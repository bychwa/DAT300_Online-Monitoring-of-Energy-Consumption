(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"power-spout" (python-spout-spec
          options
          "spouts.power.PowerSpout"
          ["socket" "power"]
          )
    }
    ;; bolt configuration
    {"count-bolt" (python-bolt-spec
          options
          {"power-spout" :shuffle}
          "bolts.power.PowerCounter"
          ["socket" "count"]
          :p 2
          )
    }
  ]
)
