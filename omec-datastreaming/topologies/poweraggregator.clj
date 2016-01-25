(ns poweraggregator
  (:use     [streamparse.specs])
  (:gen-class))

(defn poweraggregator [options]
   [
    ;; power spout configuration; takes in values from the local server
    {"power-spout" (python-spout-spec
          options
          "spouts.powerspout.PowerSpout"
          ["socket" "power" "email" "threshold"]
          )
    }
    ;; count bolt configuration; takes in values from the power-spout
    {"count-bolt" (python-bolt-spec
          options
          {"power-spout" :shuffle}
          "bolts.powerbolt.PowerCounter"
          ["socket" "count"]
          :p 2
          )
    }
  ]
)