# Звіт

## Звіт з мережі виглядає наступним чином:

### 🔹 Maximum Flow Through the Network: 115

➡️ Terminal 1:
→ Depo 1: 25
→ Depo 2: 20
→ Depo 3: 15

➡️ Depo 1:
→ Store 1: 15
→ Store 2: 10

➡️ Depo 2:
→ Store 4: 15
→ Store 5: 10
→ Store 6: 5

➡️ Depo 3:
→ Store 7: 20
→ Store 8: 10

➡️ Terminal 2:
→ Depo 2: 10
→ Depo 3: 15
→ Depo 4: 30

➡️ Depo 4:
→ Store 10: 20
→ Store 11: 10

➡️ Store 1:
→ Sink: 15

➡️ Store 2:
→ Sink: 10

➡️ Store 4:
→ Sink: 15

➡️ Store 5:
→ Sink: 10

➡️ Store 6:
→ Sink: 5

➡️ Store 7:
→ Sink: 20

➡️ Store 8:
→ Sink: 10

➡️ Store 10:
→ Sink: 20

➡️ Store 11:
→ Sink: 10

➡️ Source:
→ Terminal 1: 60
→ Terminal 2: 55

### 📈 Edge Utilization:

Terminal 1 → Depo 1: 100.00% (25/25)
Terminal 1 → Depo 2: 100.00% (20/20)
Terminal 1 → Depo 3: 100.00% (15/15)
Depo 1 → Store 1: 100.00% (15/15)
Depo 1 → Store 2: 100.00% (10/10)
Depo 1 → Store 3: 0.00% (0/20)
Depo 2 → Store 4: 100.00% (15/15)
Depo 2 → Store 5: 100.00% (10/10)
Depo 2 → Store 6: 20.00% (5/25)
Depo 3 → Store 7: 100.00% (20/20)
Depo 3 → Store 8: 66.67% (10/15)
Depo 3 → Store 9: 0.00% (0/10)
Terminal 2 → Depo 3: 100.00% (15/15)
Terminal 2 → Depo 4: 100.00% (30/30)
Terminal 2 → Depo 2: 100.00% (10/10)
Depo 4 → Store 10: 100.00% (20/20)
Depo 4 → Store 11: 100.00% (10/10)
Depo 4 → Store 12: 0.00% (0/15)
Depo 4 → Store 13: 0.00% (0/5)
Depo 4 → Store 14: 0.00% (0/10)
Store 1 → Sink: 0.00% (15/inf)
Store 2 → Sink: 0.00% (10/inf)
Store 3 → Sink: 0.00% (0/inf)
Store 4 → Sink: 0.00% (15/inf)
Store 5 → Sink: 0.00% (10/inf)
Store 6 → Sink: 0.00% (5/inf)
Store 7 → Sink: 0.00% (20/inf)
Store 8 → Sink: 0.00% (10/inf)
Store 9 → Sink: 0.00% (0/inf)
Store 10 → Sink: 0.00% (20/inf)
Store 11 → Sink: 0.00% (10/inf)
Store 12 → Sink: 0.00% (0/inf)
Store 13 → Sink: 0.00% (0/inf)
Store 14 → Sink: 0.00% (0/inf)
Source → Terminal 1: 0.00% (60/inf)
Source → Terminal 2: 0.00% (55/inf)

Зі звіту ми можемо побачити максимальний пропусну затність як усієї мережі (Maximum Flow Through the Network: 115), так і до окремих складів/магазинів.  
Окремо зі звіту можна побачити як модернізувати мережу. З графи Edge Utilization можна зрозуміти які треьа додати канали, акі розширити, для збільшення пропускрої здатності.

## Відповіді на питання:

1. Які термінали забезпечують найбільший потік товарів до магазинів?  
   Термінал 1 85, тоді як Термінал тільки 30

2. Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?  
   Depo 4 → Store 13: 5
   Depo 4 → Store 14: 10
   Depo 3 → Store 9: 10
   Depo 4 → Store 12: 15

Не використані:
Depo 3 → Store 9 (10), Depo 4 → Store 13 (5)

Store 12, Store 13, Store 14

3. Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?  
   Store 3 (0/20)
   Store 9 (0/10)
   Store 12 (0/15)
   Store 13 (0/5)
   Store 14 (0/10)

4. Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі?  
   Так, а саме  
   Depo 1 → Store 3 (0/20)  
   Depo 2 → Store 6 (5/25, 20%)  
   Depo 3 → Store 9 (0/10)  
   Depo 4 → Store 12 (0/15), Store 13 (0/5), Store 14 (0/10)

   Розширивши ці місця, ми отримаємо більший потік.
