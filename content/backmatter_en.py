# -*- coding: utf-8 -*-
"""English front/back matter."""

HOW_TO_USE = dict(
    title="How to use this book",
    kicker="Read this page before chapter one",
    sections=[
        dict(h="Who this book is for"),
        dict(p="You need no prior knowledge. Chapter 1 assumes you have never opened a chart. If you already trade, Parts II to IV will give you a vocabulary and a rule set for what you are already looking at, and Part V will show you how the pieces combine into a plan."),
        dict(h="The three passes"),
        dict(bullets=[
            "**Pass 1 — Read.** Read Parts I and II straight through without stopping to memorise. Aim to understand the *shape* of the argument: context, structure, liquidity, execution.",
            "**Pass 2 — Work.** Return to each chapter with the Workbook open and complete the exercises. This is where most of the learning happens, and it is the pass most readers skip.",
            "**Pass 3 — Apply.** Use Part V and Part VII as a field manual: plan real (or replayed) charts using the A–B–C framework and record every attempt in the journal template.",
        ], marker="do"),
        dict(h="The recurring teaching structure"),
        dict(p="Every concept chapter follows the same eleven-part structure, so you always know where you are:"),
        dict(bullets=[
            "A beginner-friendly definition, then why the concept matters.",
            "What it looks like on a candle chart, with an annotated figure.",
            "Step-by-step recognition rules, numbered so you can check them off.",
            "At least one bullish and one bearish worked example where relevant.",
            "Common beginner mistakes, and the invalidation conditions that prove you wrong.",
            "A practical exercise, followed immediately by the answer and explanation.",
        ], marker="info"),
        dict(h="Companion blocks"),
        dict(p="Many chapters end with a small dark panel containing QR codes for the free TIGERFX Academy platform. They are optional: nothing in the book depends on them. **WATCH IT** links to an animated lesson, **TRY IT** to the chart simulator, **TEST YOURSELF** to scenario practice, and **REVIEW** to a lesson covering common mistakes. Every code points to a page that was verified to exist when this edition was produced."),
        dict(h="How to read the figures"),
        dict(p="All charts in this book are marked **SYNTHETIC**. They are generated price series built for teaching, not screenshots of historical gold. This is stated deliberately and prominently, because a chart presented without that label invites the reader to believe a hypothetical setup was a real, verified outcome."),
        dict(bullets=[
            "Where a figure distinguishes analysis-time information from later confirmation, a dashed **cut-off line** marks the boundary. Everything to its right is drawn dimmed: it was not available to the analyst at the time.",
            "Possible future paths are drawn as faint dashed projections and labelled as such. They are illustrations of branches, never forecasts.",
            "Gold prices on the vertical axis are illustrative but internally consistent: the arithmetic in the examples matches the levels drawn.",
        ], marker="do"),
        dict(h="What this book will not do"),
        dict(p="It will not promise a win rate, a monthly return, or that any pattern reveals institutional intent. It will not present a hypothetical setup as a verified strategy. Part VII explains why those promises are not honest, and gives you a method for measuring your own results instead."),
    ],
)

NOTATION = dict(
    title="Notation, data and honesty rules",
    kicker="The conventions this handbook uses, stated once",
    sections=[
        dict(h="Terminology"),
        dict(p="Smart Money Concepts (SMC) terminology is not standardised. Different educators use CHoCH, MSS and *structure shift* to mean slightly different things, and there is no industry authority to settle it. Rather than pretend otherwise, each concept in this book is given an **operational definition** — a definition you can apply and check — together with a note that other authors may label the same event differently."),
        dict(table=(["Term used here", "Operational definition in this book"], [
            ["BOS", "A candle close beyond the most recent confirmed swing point, in the direction of the prevailing structure"],
            ["CHoCH", "The first candle close against the prevailing structure beyond the last protected swing"],
            ["MSS", "CHoCH accompanied by displacement and, usually, an immediately preceding liquidity sweep"],
            ["Sweep", "Price trades beyond a level and closes back inside it on the analysis timeframe"],
            ["Run", "Price closes beyond a level and continues, holding beyond it or retesting from the new side"],
            ["FVG", "Three-candle imbalance: candle 1's range does not overlap candle 3's range, with candle 2 as displacement"],
            ["Order block", "The last opposing candle before a displacement that breaks structure"],
        ])),
        dict(h="Data"),
        dict(p="Gold (XAUUSD) is quoted to two decimals throughout. One pip = 0.01, one point = 0.001 unless a broker states otherwise. Pip values assume a **100-ounce standard contract** (0.01 lot = 1 ounce = USD 1.00 per pip). Chapter 37 explains how to verify your own broker's contract size, because some use 10-ounce lots."),
        dict(h="Pips and dollars"),
        dict(p="Distances are given in pips with the dollar equivalent in brackets where useful, for example 64 pips (6.40). Prices are written with two decimals, using a comma thousands separator: 2,355.80."),
        dict(h="Session times"),
        dict(p="All session times are **Malaysian time (MYT, UTC+8)** because the primary market of this edition is Malaysia. Brokers on other server times will show different daily candle boundaries — Chapter 16 explains the consequence for previous-day levels."),
        dict(h="The honesty rules"),
        dict(bullets=[
            "**Observable versus inferred.** Price data is observable. Liquidity pools, institutional intent and *hidden orders* are inferred or unverifiable. The book labels which is which — see the table in Chapter 13.",
            "**No hindsight.** Where a figure could tempt the reader to think an entry was obvious before it developed, a cut-off line is drawn and the later candles are dimmed.",
            "**Synthetic figures.** Every chart is generated price data and is labelled SYNTHETIC in the figure header, footer and caption.",
            "**No performance claims.** No win rate, return or success rate is claimed for any setup. Volatility, slippage, spread and human error make such claims meaningless without a verified sample.",
            "**Reproducible arithmetic.** Every numerical example can be checked: the formula and inputs are always shown. Several are re-checked in the answer key of Chapter 49.",
        ], marker="do"),
        dict(h="Symbols used in the figures"),
        dict(table=(["Symbol or colour", "Meaning"], [
            ["GOLD chip", "A liquidity level or entry price"],
            ["CYAN chip", "A confirmation, an information event, or the *B* phase"],
            ["GREEN", "Bullish structure, candle, zone or outcome"],
            ["RED", "Bearish structure, candle, zone or outcome"],
            ["AMBER", "Unconfirmed or presumed event (for example a wick break)"],
            ["Dashed vertical line", "Cut-off: information after this line was not available during analysis"],
            ["Faint dashed fan", "Possible future paths — an illustration, not a forecast"],
        ])),
    ],
)

GLOSSARY = [
    ("Acceptance", "Price closing beyond a level and holding there, rather than merely trading through it with a wick."),
    ("Asian range", "The high and low formed during the Asian session (roughly 08:00–15:00 MYT for gold), used as a pre-planned liquidity reference."),
    ("Ask (offer)", "The price at which the market will sell to you; the higher of the two quoted prices."),
    ("ATR", "Average True Range: a measure of typical candle range, sometimes used to set volatility-adjusted stops."),
    ("Balance", "A price area where both sides have been traded evenly; the opposite of an imbalance."),
    ("Base", "A short cluster of overlapping candles preceding an impulsive move (see RBD and DBR)."),
    ("Bid", "The price at which the market will buy from you; the lower of the two quoted prices."),
    ("BOS (Break of Structure)", "A candle close beyond the most recent confirmed swing point, in the direction of the prevailing structure."),
    ("Break-even stop", "Moving the stop-loss to the entry price once a trade is in profit. It reduces loss size but often reduces average win."),
    ("BSL (Buy-Side Liquidity)", "Resting orders above the market — buy stops from breakout traders and stop-losses of short positions."),
    ("CFD", "Contract for Difference: a derivative that pays the difference in price between opening and closing, without owning the asset."),
    ("CHoCH (Change of Character)", "The first candle close against the prevailing structure, beyond the last protected swing point."),
    ("Commission", "A broker fee charged per lot traded, separate from the spread."),
    ("Contract size", "The quantity represented by one standard lot. For gold this is usually 100 troy ounces."),
    ("Cut-off line", "In this book's figures, a dashed vertical line separating information available during analysis from later confirmation."),
    ("Dealing range", "The swing high and swing low that contain the price action currently being analysed."),
    ("Demand zone", "An area from which price departed upward with force; the body of the last down candle before a bullish impulse."),
    ("Displacement", "An impulsive move of wide-bodied candles with small wicks, usually leaving an imbalance."),
    ("Discount", "The lower half of a dealing range, below equilibrium; the preferred area for longs."),
    ("Drawdown", "The decline in account equity from a peak, usually expressed as a percentage."),
    ("Equilibrium", "The 50% level of a dealing range, separating premium from discount."),
    ("EQH / EQL", "Equal highs or equal lows: two or more pivots within a defined tolerance, creating a liquidity cluster."),
    ("Expectancy", "The average result per trade in R multiples: (win% × average win) − (loss% × average loss)."),
    ("External structure", "The swings that define the range price is travelling in — the outer boundaries."),
    ("Failed breakout", "A move beyond a level that returns inside it, trapping breakout traders and triggering stops."),
    ("Fibonacci retracement", "A tool that divides a completed leg into ratios (0.382, 0.5, 0.618, 0.705) to locate pullbacks."),
    ("FVG (Fair Value Gap)", "A three-candle imbalance where the first and third candles' ranges do not overlap."),
    ("HH / HL", "Higher high and higher low: the two labels that together define a bullish structure."),
    ("Imbalance", "A price band that was traded through rather than traded in; the mechanical cause of an FVG."),
    ("Internal structure", "The smaller swings inside the external range; the structure a pullback is made of."),
    ("Invalidation", "The price at which the reason for a trade no longer exists; distinct from, and usually just beyond, the stop-loss order."),
    ("Leverage", "The ratio between position value and account capital. It does not increase risk by itself; position size does."),
    ("Liquidity", "The ease of transacting size without moving price. In SMC usage, also the clusters of resting orders around obvious levels."),
    ("Liquidity run", "Price closing through a level and accepting beyond it, rather than rejecting it."),
    ("Liquidity sweep", "Price trading beyond a level and closing back inside it — a visit, not an acceptance."),
    ("Lot", "The unit of contract size. 1.00 standard lot of gold is normally 100 ounces."),
    ("LTF / HTF", "Lower and higher timeframe. LTFs give timing; HTFs give direction."),
    ("Margin", "The deposit locked by the broker while a position is open."),
    ("Mitigation", "The consumption of resting orders at a zone by successive retests, reducing its future reaction strength."),
    ("MSS (Market Structure Shift)", "In this book: a CHoCH accompanied by displacement and, usually, a preceding sweep."),
    ("Order block", "The last opposing candle before a displacement that breaks structure; a descriptive label, not proof of institutional orders."),
    ("PDH / PDL", "Previous day's high and low, measured on your broker's daily candle boundaries."),
    ("Pip", "The standard smallest quoted increment. For gold quoted to two decimals, 1 pip = 0.01."),
    ("Point", "Usually one tenth of a pip (0.001 on gold)."),
    ("Premium", "The upper half of a dealing range, above equilibrium; the preferred area for shorts."),
    ("PWH / PWL", "Previous week's high and low."),
    ("Process score", "A mark for rule compliance on a trade (setup named, four numbers written, risk respected, session rules followed), independent of profit."),
    ("R multiple", "Result expressed in units of initial risk: +2R means twice the amount risked was gained."),
    ("RBD / DBR", "Rally–Base–Drop (supply) and Drop–Base–Rally (demand): three-part zone anatomy."),
    ("Reclaim", "Price closing back on the original side of a level after trading beyond it."),
    ("Retest", "A return to a broken level or zone after the break, to see whether it holds from the new side."),
    ("Reward-to-risk (R:R)", "Target distance divided by stop distance. Costs should be included before judging it."),
    ("Slippage", "The difference between the requested and the filled price, common in fast markets."),
    ("Spread", "The difference between the bid and the ask; a cost paid on entry."),
    ("SSL (Sell-Side Liquidity)", "Resting orders below the market — sell stops from breakdown traders and stop-losses of long positions."),
    ("Stop-loss", "An order that closes a position at a specified loss level. It becomes a market order when triggered and is not a guaranteed price."),
    ("Supply zone", "An area from which price departed downward with force; the body of the last up candle before a bearish impulse."),
    ("Swap", "Overnight financing charged or credited on a position held past the daily rollover."),
    ("Swing high / low", "A candle whose high (or low) is the extreme within a defined neighbourhood of candles on each side."),
    ("Take profit (TP)", "An order that closes a position at a target level."),
    ("Trailing stop", "A stop moved as the trade progresses. Structural trailing moves it only when structure moves."),
    ("XAUUSD", "The price of one troy ounce of gold in US dollars."),
]

REFERENCES_INTRO = (
    "This handbook is an educational synthesis, not a research paper. The sources below were selected because they are "
    "stable, verifiable and relevant to the claims made in the text: market mechanics, risk arithmetic, the evidence "
    "base for technical analysis, and the behavioural research behind Part VI. They are listed so that a reader can "
    "check the underlying ideas independently. Where a claim in this book rests on a specific source, the source is "
    "named. Where a claim is the author's interpretation — most of Smart Money Concepts — it is presented as such "
    "rather than attributed to a study that does not exist."
)

REFERENCES = [
    ("Bank for International Settlements (2022). *Triennial Central Bank Survey: Foreign exchange turnover in April 2022*.",
     "Context for the size and structure of the global FX market, and for the concentration of activity in the London and New York sessions used in Chapter 1."),
    ("World Gold Council. *Gold market statistics and demand trends* (annual and quarterly reports).",
     "Background on gold's role as a store of value and on the drivers referenced in Chapter 1."),
    ("CME Group. *COMEX Gold Futures (GC) contract specifications*.",
     "The 100 troy ounce contract convention that underlies the pip-value arithmetic in Chapters 1, 5 and 37."),
    ("European Securities and Markets Authority (ESMA). *Product intervention measures on contracts for difference* (2018, made permanent by national regulators).",
     "The leverage limits and risk warnings that shape the retail CFD environment described in Chapters 3 and 5."),
    ("UK Financial Conduct Authority. *PS19/18: Restrictions on the sale of contracts for differences*.",
     "A parallel regulatory treatment of retail leverage limits, used for the leverage discussion in Chapter 5."),
    ("Hull, J. C. *Options, Futures, and Other Derivatives*. Pearson.",
     "Standard reference for futures mechanics, margin, contango and the cost-of-carry logic behind swap (Chapter 40)."),
    ("Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.",
     "The classical treatment of support, resistance, trends and chart patterns that Chapters 4 and 18 compare with SMC usage."),
    ("Lo, A. W., Mamaysky, H., & Wang, J. (2000). Foundations of technical analysis: Computational algorithms, statistical inference, and empirical implementation. *Journal of Finance*, 55(4).",
     "Evidence that some chart patterns carry modest statistical information — and the methodological caution that accompanies it."),
    ("Sullivan, R., Timmermann, A., & White, H. (1999). Data-snooping, technical trading rule performance, and the bootstrap. *Journal of Finance*, 54(5).",
     "The data-snooping problem: why a rule that looks excellent on the past may be noise. Directly informs Chapter 47 (overfitting)."),
    ("Aronson, D. R. (2007). *Evidence-Based Technical Analysis*. Wiley.",
     "A disciplined framework for testing trading rules without hindsight or selection bias; the model for Chapter 47."),
    ("Tharp, V. K. (2006). *Trade Your Way to Financial Freedom* (2nd ed.). McGraw-Hill.",
     "Position sizing, R multiples and expectancy — the arithmetic framework of Chapters 5, 37, 38 and 41."),
    ("Douglas, M. (2000). *Trading in the Zone*. Prentice Hall.",
     "Probabilistic thinking and the psychology of executing a rule set under uncertainty (Chapter 42)."),
    ("Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.",
     "The cognitive biases — loss aversion, recency, confirmation — that Chapters 41 and 42 translate into practical protocols."),
    ("Barber, B. M., & Odean, T. (2000). Trading is hazardous to your wealth: The common stock investment performance of individual investors. *Journal of Finance*, 55(2).",
     "Empirical evidence that frequent trading degrades individual returns; context for the cost arithmetic in Chapters 38 and 40."),
    ("Malkiel, B. G. *A Random Walk Down Wall Street* (most recent edition). W. W. Norton.",
     "The efficient-market counterargument that a serious reader should understand before assuming any pattern is an edge."),
    ("Securities Commission Malaysia and Bank Negara Malaysia consumer alerts on unauthorised forex and gold trading schemes.",
     "Local regulatory context for the risk disclosures, relevant to the Malaysian readership of this edition."),
]

REFERENCES_NOTE = (
    "**On SMC terminology.** There is no peer-reviewed literature that defines Smart Money Concepts as used in retail "
    "education, and no published study demonstrates that *liquidity sweeps* or *order blocks* reveal institutional "
    "order flow. The definitions in this book are therefore operational: they describe price behaviour that can be "
    "observed, and they are applied consistently so that the rules can be tested. Readers who encounter different "
    "definitions elsewhere should treat the difference as a terminology matter, not as a contradiction of the price "
    "data itself."
)

DISCLAIMER = dict(
    title="Risk disclosure",
    kicker="Please read before acting on anything in this book",
    sections=[
        dict(h="Educational purpose"),
        dict(p="This publication is provided for education only. It is not financial advice, not a recommendation to buy or sell any instrument, and not a solicitation to open an account with any broker. TIGERFX Academy is an education provider, not a licensed financial adviser, and does not manage money for readers."),
        dict(h="The risk of loss is real"),
        dict(p="Trading foreign exchange, gold and contracts for difference carries a substantial risk of loss and is not suitable for everyone. Leverage magnifies both gains and losses, and you may lose more than your initial deposit depending on the instrument, your broker and your jurisdiction. You should never trade money you cannot afford to lose entirely."),
        dict(bullets=[
            "Retail traders frequently lose money. Regulatory disclosures in several jurisdictions report that a majority of retail CFD accounts lose money.",
            "Past performance — including any example in this book — does not indicate future results.",
            "No setup, framework or rule set can remove the possibility of loss. Every trade in this book has an invalidation condition precisely because it can be wrong.",
        ], marker="mistake"),
        dict(h="Limitations of examples"),
        dict(p="All charts are synthetic data generated for teaching. Numerical examples are illustrative and computed from the drawn levels; they are not records of trades taken, and they are not evidence of profitability. Where a case study shows a losing trade, it is included deliberately because valid setups lose."),
        dict(h="Execution, broker and technology risk"),
        dict(p="Spreads, slippage, commission, swap and platform outages affect real results in ways that a chart cannot show. Stop-loss orders are not guaranteed; price can gap beyond them. Different brokers quote slightly different prices. Before trading, verify contract specifications, leverage, margin requirements and execution policy with your own broker."),
        dict(h="Jurisdiction"),
        dict(p="Regulation of retail derivatives varies widely. Readers in Malaysia should consult the Securities Commission Malaysia and Bank Negara Malaysia for the current regulatory position, and readers elsewhere should consult their own regulator. Nothing in this book is intended to contravene local law."),
        dict(h="No guarantee of accuracy"),
        dict(p="Every effort has been made to check the arithmetic, terminology and figure labels in this edition, and the accompanying production report documents that work. Errors can still exist; corrections are welcome through the TIGERFX Academy website. Neither the author nor the publisher accepts liability for any loss arising from use of this material."),
        dict(h="Seek independent advice"),
        dict(p="If you are unsure whether trading is appropriate for you, consult an independent, licensed financial adviser who can assess your circumstances. Do not rely on social media, courses or books — including this one — as a substitute for personal financial advice."),
    ],
)

ABOUT = dict(
    title="About TIGERFX Academy",
    kicker="Learn. Analyze. Practice. Understand.",
    sections=[
        dict(p="TIGERFX Academy is a bilingual (Bahasa Melayu and English) trading education platform built for beginners who want to understand markets rather than memorise signals. Its curriculum follows the same five-level path as this handbook: market basics, reading price action, Smart Money Concepts, strategy and execution, and an advanced practice lab."),
        dict(p="The platform provides animated lessons, a chart simulator with drawing tools and bar replay, scenario-based practice with reasoning feedback, and a risk-first toolkit that includes a position-sizing sandbox and a session clock in Malaysian time. It is free to use, requires no signup, and uses synthetic teaching data throughout."),
        dict(h="What the Academy deliberately does not do"),
        dict(bullets=[
            "It does not promise returns, win rates or *signals*.",
            "It does not require you to open a broker account to learn.",
            "It does not present synthetic results as performance.",
        ], marker="mistake"),
        dict(h="Where to continue"),
        dict(p="Start with the learning path and work through the level that matches your current understanding. Readers of this handbook will find Level 3 most useful for drilling the SMC concepts in Parts II to IV, and the simulator's bar-replay mode ideal for the 100-setup practice recommended in Chapter 47."),
    ],
)

INDEX_TERMS = [
    "Acceptance", "Asian range", "BOS", "Break-even", "BSL", "CHoCH", "Cut-off", "Dealing range",
    "Demand zone", "Displacement", "Discount", "Drawdown", "Equilibrium", "EQH", "EQL", "Expectancy",
    "External structure", "Failed breakout", "Fibonacci", "FVG", "HH/HL", "Imbalance", "Internal structure",
    "Invalidation", "Leverage", "Liquidity", "Liquidity run", "Liquidity sweep", "Lot", "Margin",
    "Mitigation", "MSS", "Order block", "PDH/PDL", "Pip", "Premium", "Process score", "R multiple",
    "RBD/DBR", "Reclaim", "Retest", "Reward-to-risk", "Slippage", "Spread", "SSL", "Stop-loss", "Supply zone",
    "Swap", "Swing high", "Swing low", "Trailing stop", "XAUUSD",
]
