(define (problem p1-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc{i}{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc{i}{j} and loc{h}{k}
  (:objects
    loc31 loc12 loc22 loc32 loc42 loc23 loc33 loc24 loc34 loc44 - location
    key1 key2 key3 key4 - key
    c3132 c1222 c2232 c3242 c2223 c3233 c2333 c2324 c3334 c2434 c3444 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc12)
    (arm-free)

    ; Locationg <> Corridor Connections
    (corridor-valid loc31 loc32 c3132)
    (corridor-valid loc12 loc22 c1222)
    (corridor-valid loc22 loc32 c2232)
    (corridor-valid loc32 loc42 c3242)
    (corridor-valid loc22 loc23 c2223)
    (corridor-valid loc32 loc33 c3233)
    (corridor-valid loc23 loc33 c2333)
    (corridor-valid loc23 loc24 c2324)
    (corridor-valid loc33 loc34 c3334)
    (corridor-valid loc24 loc34 c2434)
    (corridor-valid loc34 loc44 c3444)
        
    (corridor-valid loc32 loc31 c3132)
    (corridor-valid loc22 loc12 c1222)
    (corridor-valid loc32 loc22 c2232)
    (corridor-valid loc42 loc32 c3242)
    (corridor-valid loc23 loc22 c2223)
    (corridor-valid loc33 loc32 c3233)
    (corridor-valid loc33 loc23 c2333)
    (corridor-valid loc24 loc23 c2324)
    (corridor-valid loc34 loc33 c3334)
    (corridor-valid loc34 loc24 c2434)
    (corridor-valid loc44 loc34 c3444)
    
    ; Locations the hero can get to
    (hero-to loc44)
    (hero-to loc31)
    (hero-to loc12)
    (hero-to loc22)
    (hero-to loc32)
    (hero-to loc42)
    (hero-to loc23)
    (hero-to loc33)
    (hero-to loc24)
    (hero-to loc34)

    ; Key locations
    (key-have loc22 key1)
    (key-have loc24 key2)
    (key-have loc42 key3)
    (key-have loc44 key4)

    ; Locked corridors
    (lock-exist c2324)
    (lock-exist c2434)
    (lock-exist c3132)
    (lock-exist c3242)
    (lock-exist c3444)

    ; Risky corridors
    (corridor-risky c2324)
    (corridor-risky c2434)

    ; Key colours
    (is-keyright red key1)
    (is-keyright yellow key2)
    (is-keyright rainbow key3)
    (is-keyright purple key4)
    
    ; Key usage properties (one use, two use, etc)
    (oneusedkey key3)
    (oneusedkey key4)
    (twousedkey key2)
    (mutiusedkey key1)
    
    ; Lock colours
    (corridor-lockcolor c2324 red)
    (corridor-lockcolor c2434 red)
    (corridor-lockcolor c3132 rainbow)
    (corridor-lockcolor c3444 yellow)
    (corridor-lockcolor c3242 purple)
    
    ; Locked corridors to a location
    (corridor-connect loc23 c2324)
    (corridor-connect loc24 c2324)
    (corridor-connect loc24 c2434)
    (corridor-connect loc34 c2434)
    (corridor-connect loc34 c3444)
    (corridor-connect loc32 c3242)
    (corridor-connect loc32 c3132)

  )
  (:goal
    (and
       (hero-at loc31)

      ; Hero's final location goes here
    )
  )

)
