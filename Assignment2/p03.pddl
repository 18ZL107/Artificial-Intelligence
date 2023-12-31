(define (problem p3-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc{i}{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc{i}{j} and loc{h}{k}
  (:objects
    loc34 loc45 loc12 loc22 loc32 loc33 loc25 loc13 loc21 loc14 loc35 loc24 loc44 loc23 loc43 - location
    c2122 c1222 c2232 c1213 c1223 c2223 c3223 c3233 c1323 c2333 c1314 c2314 c2324 c2334 c3334 c1424 c2434 c2425 c2535 c3545 c4544 c4443 - corridor
    key1 key2 key3 key4 key5 key6 - key
  )

  (:init
    
    ; Hero location and carrying status
    (hero-at loc21)
    (arm-free)

    ; Locationg <> Corridor Connections
    (corridor-valid loc21 loc22 c2122)
    (corridor-valid loc12 loc22 c1222)
    (corridor-valid loc22 loc32 c2232)
    (corridor-valid loc12 loc13 c1213)
    (corridor-valid loc12 loc23 c1223)
    (corridor-valid loc22 loc23 c2223)
    (corridor-valid loc32 loc23 c3223)
    (corridor-valid loc32 loc33 c3233)
    (corridor-valid loc13 loc23 c1323)
    (corridor-valid loc23 loc33 c2333)
    (corridor-valid loc13 loc14 c1314)
    (corridor-valid loc23 loc14 c2314)
    (corridor-valid loc23 loc24 c2324)
    (corridor-valid loc23 loc34 c2334)
    (corridor-valid loc33 loc34 c3334)
    (corridor-valid loc14 loc24 c1424)
    (corridor-valid loc24 loc34 c2434)
    (corridor-valid loc24 loc25 c2425)
    (corridor-valid loc25 loc35 c2535)
    (corridor-valid loc35 loc45 c3545)
    (corridor-valid loc45 loc44 c4544)
    (corridor-valid loc44 loc43 c4443)

    (corridor-valid loc22 loc21 c2122)
    (corridor-valid loc22 loc12 c1222)
    (corridor-valid loc32 loc22 c2232)
    (corridor-valid loc13 loc12 c1213)
    (corridor-valid loc23 loc12 c1223)
    (corridor-valid loc23 loc22 c2223)
    (corridor-valid loc23 loc32 c3223)
    (corridor-valid loc33 loc32 c3233)
    (corridor-valid loc23 loc13 c1323)
    (corridor-valid loc33 loc23 c2333)
    (corridor-valid loc14 loc13 c1314)
    (corridor-valid loc14 loc23 c2314)
    (corridor-valid loc24 loc23 c2324)
    (corridor-valid loc34 loc23 c2334)
    (corridor-valid loc34 loc33 c3334)
    (corridor-valid loc24 loc14 c1424)
    (corridor-valid loc34 loc24 c2434)
    (corridor-valid loc25 loc24 c2425)
    (corridor-valid loc35 loc25 c2535)
    (corridor-valid loc45 loc35 c3545)
    (corridor-valid loc44 loc45 c4544)
    (corridor-valid loc43 loc44 c4443)

    ; Locations the hero can get to
    (hero-to loc12)
    (hero-to loc13)
    (hero-to loc14)
    (hero-to loc21)
    (hero-to loc22)
    (hero-to loc23)
    (hero-to loc24)
    (hero-to loc25)
    (hero-to loc32)
    (hero-to loc33)
    (hero-to loc34)
    (hero-to loc35)
    (hero-to loc43)
    (hero-to loc44)
    (hero-to loc45)

    ; Key locations
    (key-have loc21 key1)
    (key-have loc23 key2)
    (key-have loc23 key3)
    (key-have loc23 key4)
    (key-have loc23 key5)
    (key-have loc44 key6)

    ; Locked corridors
    (lock-exist c1223)
    (lock-exist c2223)
    (lock-exist c3223)
    (lock-exist c1323)
    (lock-exist c2333)
    (lock-exist c2314)
    (lock-exist c2324)
    (lock-exist c2334)
    (lock-exist c2425)
    (lock-exist c2535)
    (lock-exist c3545)
    (lock-exist c4544)
    (lock-exist c4443)

    ; Risky corridors
    (corridor-risky c1223)
    (corridor-risky c2223)
    (corridor-risky c3223)
    (corridor-risky c1323)
    (corridor-risky c2333)
    (corridor-risky c2314)
    (corridor-risky c2324)
    (corridor-risky c2334)

    ; Key colours
    (is-keyright red key1)
    (is-keyright purple key2)
    (is-keyright green key3)
    (is-keyright purple key4)
    (is-keyright green key5)
    (is-keyright rainbow key6)

    ; Key usage properties (one use, two use, etc)
    (mutiusedkey key1)
    (oneusedkey key2)
    (oneusedkey key3)
    (oneusedkey key4)
    (oneusedkey key5)
    (oneusedkey key6)

    ; Lock colours
    (corridor-lockcolor c1223 red)
    (corridor-lockcolor c2223 red)
    (corridor-lockcolor c3223 red)
    (corridor-lockcolor c1323 red)
    (corridor-lockcolor c2333 red)
    (corridor-lockcolor c2314 red)
    (corridor-lockcolor c2324 red)
    (corridor-lockcolor c2334 red)
    (corridor-lockcolor c2425 purple)
    (corridor-lockcolor c2535 green)
    (corridor-lockcolor c3545 purple)
    (corridor-lockcolor c4544 green)
    (corridor-lockcolor c4443 rainbow)

    ; Locked corridors to a location
    (corridor-connect loc12 c1223)
    (corridor-connect loc23 c1223)
    (corridor-connect loc22 c2223)
    (corridor-connect loc23 c2223)
    (corridor-connect loc32 c3223)
    (corridor-connect loc23 c3223)
    (corridor-connect loc13 c1323)
    (corridor-connect loc23 c1323)
    (corridor-connect loc33 c2333)
    (corridor-connect loc23 c2333)
    (corridor-connect loc14 c2314)
    (corridor-connect loc23 c2314)
    (corridor-connect loc24 c2324)
    (corridor-connect loc23 c2324)
    (corridor-connect loc34 c2334)
    (corridor-connect loc23 c2334)
    (corridor-connect loc24 c2425)
    (corridor-connect loc25 c2425)
    (corridor-connect loc25 c2535)
    (corridor-connect loc35 c2535)
    (corridor-connect loc35 c3545)
    (corridor-connect loc45 c3545)
    (corridor-connect loc45 c4544)
    (corridor-connect loc44 c4544)
    (corridor-connect loc44 c4443)
  )
  (:goal
    (and
      (hero-at loc43)
      ; Hero's final location goes here
    )
  )

)
