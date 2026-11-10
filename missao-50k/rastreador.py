"""Rastreador da Missão R$50k.

Registra horas, receitas e gastos por mês e avisa quando um limite de perda
ou um ponto de parada do PLANO.md é atingido.

Uso:
    python rastreador.py horas   <frente> <horas> [usd_ganhos]
    python rastreador.py receita <frente> <valor_usd> [descricao]
    python rastreador.py gasto   <valor_brl> <descricao>
    python rastreador.py teste   <nome> <passou|falhou> [nota]
    python rastreador.py status  [AAAA-MM]

Frentes: A (treinamento de IA) ou B (serviços de automação).
"""

import json
import sys
from datetime import date
from pathlib import Path

ARQUIVO = Path(__file__).with_name("registros.json")

CAMBIO = 5.40               # R$ por US$ – atualize quando quiser
IMPOSTO = 0.15              # alíquota estimada; ajuste com o contador
META_LIQUIDA_BRL = 50_000
LIMITE_GASTO = {1: 1_500, 2: 3_000}  # por mês da operação
LIMITE_PERDA_BRL = -500
CORTE_DIA_60_BRL = 8_000
HORA_MINIMA_USD = 12


def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return {"inicio": date.today().isoformat(), "eventos": []}


def salvar(dados):
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def mes_da_operacao(dados, dia):
    inicio = date.fromisoformat(dados["inicio"])
    return (dia - inicio).days // 30 + 1


def registrar(dados, tipo, **campos):
    dados["eventos"].append({"data": date.today().isoformat(), "tipo": tipo, **campos})
    salvar(dados)


def status(dados, mes=None):
    mes = mes or date.today().strftime("%Y-%m")
    eventos = [e for e in dados["eventos"] if e["data"].startswith(mes)]

    receita_usd = sum(e["usd"] for e in eventos if e["tipo"] == "receita")
    gasto_brl = sum(e["brl"] for e in eventos if e["tipo"] == "gasto")
    receita_brl = receita_usd * CAMBIO
    liquido = receita_brl * (1 - IMPOSTO) - gasto_brl

    print(f"== Mês {mes} ==")
    print(f"Receita: US${receita_usd:,.2f} (R${receita_brl:,.2f})")
    print(f"Gasto:   R${gasto_brl:,.2f}")
    print(f"Líquido estimado: R${liquido:,.2f}  ({liquido / META_LIQUIDA_BRL:.0%} da meta)")

    for frente in ("A", "B"):
        horas = [e for e in eventos if e["tipo"] == "horas" and e["frente"] == frente]
        total_h = sum(e["horas"] for e in horas)
        total_usd = sum(e.get("usd", 0) for e in horas)
        if total_h:
            hora = total_usd / total_h
            print(f"Frente {frente}: {total_h:.1f} h, US${hora:.2f}/h efetiva")
            if frente == "A" and hora < HORA_MINIMA_USD:
                print(f"  ALERTA: hora efetiva abaixo de US${HORA_MINIMA_USD}. Trocar de plataforma.")

    hoje = date.today()
    n_mes = mes_da_operacao(dados, hoje)
    limite = LIMITE_GASTO.get(n_mes)
    if limite is not None and gasto_brl > limite:
        print(f"PARE: gasto passou do limite do mês {n_mes} (R${limite:,}).")
    if liquido < LIMITE_PERDA_BRL:
        print("PARE: limite de perda mensal atingido. Congelar todo gasto.")
    dias = (hoje - date.fromisoformat(dados["inicio"])).days
    if dias >= 60 and liquido < CORTE_DIA_60_BRL:
        print("PARE: dia 60 com líquido abaixo de R$8 mil. Reavaliar o modelo.")

    testes = [e for e in dados["eventos"] if e["tipo"] == "teste"]
    if testes:
        print("Testes de validação:")
        for t in testes:
            print(f"  {t['data']} {t['nome']}: {t['resultado']} {t.get('nota', '')}")


def main(args):
    dados = carregar()
    if not args:
        print(__doc__)
        return
    cmd, resto = args[0], args[1:]
    if cmd == "horas":
        usd = float(resto[2]) if len(resto) > 2 else 0.0
        registrar(dados, "horas", frente=resto[0].upper(), horas=float(resto[1]), usd=usd)
    elif cmd == "receita":
        registrar(dados, "receita", frente=resto[0].upper(), usd=float(resto[1]),
                  descricao=" ".join(resto[2:]))
    elif cmd == "gasto":
        registrar(dados, "gasto", brl=float(resto[0]), descricao=" ".join(resto[1:]))
    elif cmd == "teste":
        registrar(dados, "teste", nome=resto[0], resultado=resto[1], nota=" ".join(resto[2:]))
    elif cmd == "status":
        status(dados, resto[0] if resto else None)
        return
    else:
        print(__doc__)
        return
    status(dados)


if __name__ == "__main__":
    main(sys.argv[1:])
