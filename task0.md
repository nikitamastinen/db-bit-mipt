## Типы баз данных
1. DragonFly - P, ведь это улучшенный Redis (Cluster), где есть возможность синхронизировать узлы (с помощью технологии master-slave) и останавливать часть, не потеряв ничего, но при этом не гарантируется доступность в любое время. Однако синхронизация с помощью метода Wait не гарантирует strong consistency исходя из асинхронной реализации, записи могут потеряться: https://redis.io/docs/management/scaling/. Однако если делать Flush и исхитриться, можно добиться CP, значительно потеряв производительность, но вроде так не делают. DragonFly по сути также реализован, разве что заменены некоторые принципы синхронизации, поэтому можно ориентироваться на Redis.
https://aws.amazon.com/ru/redis/ (P)

2. ScyllaDB - AP. По документации гарантируется доступность в любой момент и возможность безболезненно терять узлы, однако атомарное исполнение транзакций не гарантируется, также как и одинаковый результат в узлах.
https://docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html#:~:text=Scylla%2C%20as%20do%20many%20distributed,factors%20will%20reduce%20the%20third. (Схема)

3. ArenadataDB - AC. По документации утверждается соответствие ACID и High availability, отсюда, используя CAP-теорему и получаем нужное.
https://arenadata.tech/wp-content/uploads/2020/06/arenadata-profile-1.pdf (ACID, слайд 18)
https://arenadata.tech/about/news/obzor-produktovyh-relizov-za-yanvar-2023-goda/ (High availability)

