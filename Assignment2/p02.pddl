(define (problem p2-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc{i}{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc{i}{j} and loc{h}{k}
  (:objects
    loc21 loc12 loc22 loc32 loc42 loc23 - location
    key1 key2 key3 key4 - key
    c2122 c1222 c2232 c3242 c2223 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc22)
    (arm-free)

    ; Locationg <> Corridor Connections
    (corridor-valid loc21 loc22 c2122)
    (corridor-valid loc12 loc22 c1222)
    (corridor-valid loc22 loc32 c2232)
    (corridor-valid loc32 loc42 c3242)
    (corridor-valid loc23 loc22 c2223)

    (corridor-valid loc22 loc21 c2122)
    (corridor-valid loc22 loc12 c1222)
    (corridor-valid loc32 loc22 c2232)
    (corridor-valid loc42 loc32 c3242)
    (corridor-valid loc22 loc23 c2223)

    ; Locations the hero can get to
    (hero-to loc22)
    (hero-to loc21)
    (hero-to loc12)
    (hero-to loc32)
    (hero-to loc23)
    (hero-to loc42)

    ; Key locations
    (key-have loc22 key1)
    (key-have loc21 key2)
    (key-have loc23 key3)
    (key-have loc12 key4)

    ; Locked corridors
    (lock-exist c2122)
    (lock-exist c2223)
    (lock-exist c1222)
    (lock-exist c2232)
    (lock-exist c3242)

    ; No risky corridors

    ; Key colours
    (is-keyright purple key1)
    (is-keyright green key2)
    (is-keyright yellow key3)
    (is-keyright rainbow key4)

    ; Key usage properties (one use, two use, etc)
    (oneusedkey key1)
    (oneusedkey key2)
    (twousedkey key3)
    (oneusedkey key4)

    ; Lock colours
    (corridor-lockcolor c2122 purple)
    (corridor-lockcolor c2223 green)
    (corridor-lockcolor c1222 yellow)
    (corridor-lockcolor c2232 yellow)
    (corridor-lockcolor c3242 rainbow)

    ; Locked corridors to a location
    (corridor-connect loc12 c1222)
    (corridor-connect loc21 c2122)
    (corridor-connect loc22 c1222)
    (corridor-connect loc22 c2122)
    (corridor-connect loc22 c2232)
    (corridor-connect loc22 c2223)
    (corridor-connect loc23 c2223)
    (corridor-connect loc32 c2232)
    (corridor-connect loc32 c3242)
    (corridor-connect loc42 c3242)
  )
  (:goal
    (and
      (hero-at loc42)

      ; Hero's final location goes here
    )
  )

)
