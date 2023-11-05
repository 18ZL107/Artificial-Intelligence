(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Come up with your own problem instance (see assignment for details)
  ; NOTE: You _may_ use new objects for this problem only.

  ; Naming convention:
  ; - loc{i}{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc{i}{j} and loc{h}{k}
  (:objects
    loc11 loc12 loc13 loc21 loc22 loc23 loc31 loc32 loc33 - location
    c1121 c2131 c1222 c2232 c2122 c2213 c1323 c2331 c2233 - corridor
    key1 key2 key3 key4 key5 key6 key7 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc11)
    (arm-free)

    ; Locationg <> Corridor Connections
    (corridor-valid loc11 loc21 c1121)
    (corridor-valid loc21 loc31 c2131)
    (corridor-valid loc12 loc22 c1222)
    (corridor-valid loc22 loc32 c2232)
    (corridor-valid loc21 loc22 c2122)
    (corridor-valid loc22 loc13 c2213)
    (corridor-valid loc13 loc23 c1323)
    (corridor-valid loc23 loc31 c2331)
    (corridor-valid loc22 loc33 c2233)

    (corridor-valid loc21 loc11 c1121)
    (corridor-valid loc31 loc21 c2131)
    (corridor-valid loc22 loc12 c1222)
    (corridor-valid loc32 loc22 c2232)
    (corridor-valid loc22 loc21 c2122)
    (corridor-valid loc13 loc22 c2213)
    (corridor-valid loc23 loc13 c1323)
    (corridor-valid loc31 loc23 c2331)
    (corridor-valid loc33 loc22 c2233)

    ; Locations the hero can get to
    (hero-to loc11)
    (hero-to loc21)
    (hero-to loc31)
    (hero-to loc12)
    (hero-to loc22)
    (hero-to loc32)
    (hero-to loc13)
    (hero-to loc23)
    (hero-to loc33)

    ; Key locations
    (key-have loc31 key1)
    (key-have loc31 key2)
    (key-have loc31 key3)
    (key-have loc12 key4)
    (key-have loc32 key5)
    (key-have loc13 key6)
    (key-have loc13 key7)

    ; Locked corridors
    (lock-exist c2122)
    (lock-exist c1222)
    (lock-exist c2232)
    (lock-exist c2213)
    (lock-exist c1323)
    (lock-exist c2233)
    (lock-exist c2331)

    ; Risky corridors
    (corridor-risky c2213)

    ; Key colours
    (is-keyright red key1)
    (is-keyright yellow key2)
    (is-keyright purple key3)
    (is-keyright purple key4)
    (is-keyright rainbow key5)
    (is-keyright green key6)
    (is-keyright green key7)

    ; Key usage properties (one use, two use, etc)
    (mutiusedkey key1)
    (twousedkey key2)
    (oneusedkey key3)
    (oneusedkey key4)
    (oneusedkey key5)
    (oneusedkey key6)
    (oneusedkey key7)

    ; Lock colours
    (corridor-lockcolor c2122 purple)
    (corridor-lockcolor c1222 green)
    (corridor-lockcolor c2232 purple)
    (corridor-lockcolor c2213 red)
    (corridor-lockcolor c1323 yellow)
    (corridor-lockcolor c2331 green)
    (corridor-lockcolor c2233 rainbow)

    ; Locked corridors to a location
    (corridor-connect loc21 c2122)
    (corridor-connect loc31 c2331)
    (corridor-connect loc12 c1222)
    (corridor-connect loc22 c2122)
    (corridor-connect loc22 c1222)
    (corridor-connect loc22 c2232)
    (corridor-connect loc22 c2213)
    (corridor-connect loc22 c2233)
    (corridor-connect loc32 c2232)
    (corridor-connect loc13 c2213)
    (corridor-connect loc13 c1323)
    (corridor-connect loc23 c1323)
    (corridor-connect loc23 c2331)
    (corridor-connect loc33 c2233)
  )
  (:goal
    (and
      (hero-at loc33)
      ; Hero's final location goes here
    )
  )

)
