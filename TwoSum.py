from typing import List


class TwoSum:
    def TwoSum(self, numbers: List[int], target: int) -> List[int]:
        # Inizializza due puntatori, uno all'inizio e uno alla fine dell'array
        left, right = 0, len(numbers) - 1

        # Continua finché i puntatori non si incrociano
        while left < right:
            current_sum = numbers[left] + numbers[right]

            # Se trovi il target, restituisci gli indici, ricordando che sono 1-indicizzati
            if current_sum == target:
                return [left + 1, right + 1]

            # Se la somma corrente è troppo piccola, sposta il puntatore sinistro
            elif current_sum < target:
                left += 1

            # Se la somma corrente è troppo grande, sposta il puntatore destro
            else:
                right -= 1

        # Poiché la soluzione è garantita, non serve return -1
        return []