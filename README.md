# HSE ML Course Project
### Работу выполнили:  
* Литвинов Михаил
* Габидуллин Камиль
### Презентация к защите:
* https://docs.google.com/presentation/d/11PCdAiCZonasoyVw3EnaTKkEga9mveXAcscftLH1na4
### Предположительный ход работы:
* Взять сырые данные (последовательность ходов и дефолтные фичи) и обучить несколько простых моделей
* Взять последовательность оценок шахматного движка и обучить на ней простые модели
* В качестве дополнительных признаков выделить:
  * Количество резких изменений оценок шахматного движка (гипотеза: слабые шахматисты часто ошибаются, оценка движка будет скакать)
  * Количество попаданий в 1-3 линии шахматного движка (гипотеза: сильные шахматисты часто выбирают наилучший ход со стороны компьютера)
  * Сгрупировать данные по времени партии, отсечь игры с высокой разницей рейтинга у оппонентов (и в таком случа можно предсказывать рейтинг игры, а не человека)
* Обучить несколько моделей, подобрать параметры
* Написать ТГ бота, которому можно будет загрузить свою игру, а на выходе получить предположительный разряд
### Links:
* https://github.com/zhelyabuzhsky/stockfish
* https://python-chess.readthedocs.io/en/latest/pgn.html
* https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/
* https://lczero.org/blog/2020/04/wdl-head/
* https://hxim.github.io/Stockfish-Evaluation-Guide/
* https://disservin.github.io/stockfish-docs/stockfish-wiki/Developers.html#using-stockfish-in-your-own-project
* more...

