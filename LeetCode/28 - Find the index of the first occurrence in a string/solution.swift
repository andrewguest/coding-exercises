class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        // if needle is an empty string
        if needle.isEmpty {
            return 0
        }

        // if we can find the value of "needle" within "haystack" then returrn that
        if let rng = haystack.range(of: needle) {
            return rng.lowerBound.encodedOffset
        }

        // if nothing above works, then return -1
        return -1
    }
}