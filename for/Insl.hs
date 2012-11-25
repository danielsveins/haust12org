module Main where

main :: IO ()
main =
     do { putStrLn "Halló, hver et þú?"
        ; nafn <- getLine
	; putStrLn ("Góðann daginn " ++ nafn)
	}
