### Representing two categories (3/3)

Intro:

> **In pandas, a comparison can directly create a True/False feature.**

Code:

```python
df["holiday"] = df["holiday"] == "Holiday"

df["functioning_day"] = df["functioning_day"] == "Yes"
```

И ниже маленький output/example:

```text
holiday      functioning_day
True         True
False        False
False        True
True         False
```

Closing можно вообще не добавлять. Код уже достаточно ясно показывает мысль.

Мне особенно нравится, что здесь студенты увидят важную вещь: справа от `=` мы **задаём условие**, а результат этого условия становится новым representation колонки.

---

### Representing multiple categories (4/4)

Тогда текущие `(1/3)–(3/3)` становятся `(1/4)–(3/4)`, и четвёртый — implementation.

Intro:

> **In pandas, `pd.get_dummies()` creates one True/False feature for each category.**

Code прямо из notes:

```python
df = pd.get_dummies(
    df,
    columns=["season"]
)
```

Можно не переносить на три строки, если помещается:

```python
df = pd.get_dummies(df, columns=["season"])
```

И рядом/под ним output:

```text
season_winter  season_spring  season_summer  season_autumn
True           False          False          False
False          True           False          False
False          False          True           False
False          False          False          True
```

Небольшая annotation:

> `season` is removed and replaced by four new features.

Это полезно, потому что `pd.get_dummies()` делает **две вещи сразу**: создаёт dummy columns и убирает исходную `season`. Именно так это уже объясняется в notes.
