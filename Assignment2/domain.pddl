(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
    )
    
    (:types colour location corridor key)
    
    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates

        ; One predicate given for free!
        (hero-at ?loc - location)
        (hero-to ?loc - location)
        (corridor-valid ?from ?to - location ?cor - corridor)
        (lock-exist ?cor - corridor)
        (corridor-risky ?cor - corridor)
        
        (key-have ?loc - location ?k - key)
        (arm-free)
        (key-holding ?k - key)
        
        (zerousedkey ?k -key)
        (oneusedkey ?k - key )
        (twousedkey ?k - key )
        (mutiusedkey ?k - key )
        (corridor-lockcolor ?cor - corridor ?c - colour)
        (is-keyright ?c - colour ?k - key)
        (corridor-connect ?loc - location ?cor - corridor)


    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - wants to move to location ?to,
    ;    - corridor ?cor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor
    ;Effects move the hero, and collapse the corridor if it's "risky"
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and (hero-at ?from)
                           (hero-to ?to)
                           (corridor-valid ?from ?to ?cor)
                           (not (lock-exist ?cor))                           
                           )


        :effect (and 
        
                (when (and ; When the corridor is risky
                           (corridor-risky ?cor))
                           (and (hero-at ?to)
                           (not (hero-at ?from))
                           (not (corridor-valid ?from ?to ?cor))
                           (not (corridor-valid ?to ?from ?cor))
                           ))

                (when (and ; When the corridor is not risky
                           (not (corridor-risky ?cor))
                           )
                           (and (hero-at ?to)
                                (not (hero-at ?from))
                           )                           
                           )               
                )                                       
    )

    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc,
    ;    - there is a key ?k at location ?loc,
    ;    - the hero's arm is free,
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - key)

        :precondition (and (hero-at ?loc)
                           (key-have ?loc ?k)  
                           (arm-free)
        
        )
        

        :effect (and (not (key-have ?loc ?k))  
                     (not (arm-free))
                     (key-holding ?k)
        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k,
    ;    - the hero is at location ?loc
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - key)

        :precondition (and (key-holding ?k )
                           (hero-at ?loc)
                           (not (arm-free))
        
        )

        :effect (and (not (key-holding ?k ))
                     (key-have ?loc ?k)
                     (arm-free)

        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor is locked with colour ?col,
    ;    - the key ?k is if the right colour ?col,
    ;    - the hero is at location ?loc
    ;    - the corridor is connected to the location ?loc
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - key)

        :precondition (and (key-holding ?k)
                           (corridor-lockcolor ?cor ?col)
                           (is-keyright ?col ?k)
                           (hero-at ?loc)
                           (corridor-connect ?loc ?cor)
                           (not(zerousedkey ?k))

        )

        :effect (and ; When holding one use key
                     (when (oneusedkey ?k) (and (zerousedkey ?k) (not(lock-exist ?cor )) (not(corridor-connect ?loc ?cor)))
                     ) 
                     ; When holding two use key
                     (when (twousedkey ?k) (and (oneusedkey ?k) (not(lock-exist ?cor )) (not(corridor-connect ?loc ?cor)))
                     ) 
                     ; When holding multiple use key
                     (when (mutiusedkey ?k) (and (mutiusedkey ?k) (not(lock-exist ?cor )) (not(corridor-connect ?loc ?cor)))
                     ) 
                     
        )
    )

)
