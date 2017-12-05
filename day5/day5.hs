import qualified Data.Vector.Unboxed as V

main :: IO()
main = do
    s <- readFile "d5.in"
    let l =  V.fromList . map read . lines $ s :: V.Vector Int
    putStrLn $ show $ part1 0 l
    putStrLn $ show $ part2 0 l


part1 :: Int -> V.Vector Int -> Int
part1 i l | i == V.length l = 0
          | otherwise = 1 + part1 (i + (l V.! i)) (l V.// [(i, (l V.! i) + 1)])

part2 :: Int -> V.Vector Int -> Int
part2 i l | i == V.length l = 0
          | otherwise  = 1 + part2 (i + (l V.! i)) (l V.// [(i, (l V.! i) + x)])
    where x = if l V.! i < 3 then 1 else -1