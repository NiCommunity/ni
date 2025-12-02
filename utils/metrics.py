from typing import List

def _compute_binary_relevance(
    recommended_items_list: List[int], #Это список из целых чисел. Каждое целое число - музыкальный трек, который модель порекомендовала послушать пользователю.
    true_items_list: List[int], #Это список из целых чисел. Каждое целое число - музыкальный трек, который пользователь реально послушал.
) -> List[int]: #Надо вернуть список из целых чисел такой же длины, как и recommended_items_list. Для каждого трека в списке recommended_items_list надо проставить 0 или 1. Это делается
  # на основе того, был ли рекомендованный трек реально прослушан. 1 - если рекомендованный трек был реально прослушан. 0 - иначе
  # your code here:

  answer=[]

  for i in range(0, len(recommended_items_list),1):
    if recommended_items_list[i] in true_items_list:
        answer.append(1)
    else:
        answer.append(0)
  
  return answer

#################################################################################################################################################
def ap_at_k(
    recommended_items_list: List[int],
    true_items_list: List[int],
    k: int
) -> float:
  # your code here:

  #k — это количество рекомендаций, которые мы рассматриваем (первые k элементов в списке рекомендаций).

  k=min(k, len(recommended_items_list)) #Проверяем, чтобы k не оказалось больше кол-ва рекомендованных треков в recommended_items_list

  #Посчитаем p@k - precision at k.

  relevant=_compute_binary_relevance(recommended_items_list,true_items_list) #Список из нулей и единиц. Показывает угадала ли модель предложив тот или иной трек по сравнению с реально прослушанными треками

  p_at_k_list=[]


  for i in range(0,k,1):
    x=[relevant[j] for j in range(0,i+1,1)]
    l=len(x)
    a=sum(x)/l
    p_at_k_list.append(a)

  #Посчитаем P

  P=[]

  for i in range(0,k,1):
    if relevant[i]==1:
      P.append(p_at_k_list[i])
    else:
      P.append(0)

  m=len(set(true_items_list)) #Мощность множества реально прослушанных треков. Set чтобы не было повторных

  mini=min(k,m)

  if mini==0: #Чтобы не было деления на ноль
    return 0
  else:
    ap_at_k_otvet=sum(P)/mini
    return ap_at_k_otvet

  
##################################################################################
def map_at_k(
    recommended_items_lists: List[List[int]], #Это список СПИСКОВ!!! 
    true_items_lists: List[List[int]],
    k: int,
) -> float:
  """
  Computes ap@k for all buyers
  """
  assert len(recommended_items_lists) == len(true_items_lists), \
  'len(true_items_list) != len(recommended_items_list)'

  # your code here:

  N=len(true_items_lists) #Число пользователей

  ap_at_k_list=[ap_at_k(recommended_items_lists[i], true_items_lists[i],k) for i in range(0,N, 1)]

  map_at_k_otvet=sum(ap_at_k_list)/N

  return map_at_k_otvet


