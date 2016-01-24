(ns poweraggregator
  (:use     [streamparse.specs])
  (:gen-class))

(defn poweraggregator [options]
   [
    ;; spout configuration
    {"power-spout" (python-spout-spec
          options
          "spouts.power.PowerSpout"
          ["socket" "power" "email" "threshold"]
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