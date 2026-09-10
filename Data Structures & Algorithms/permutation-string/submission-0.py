class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # This process uses TWO arrays to detect if a match was succesful
        # S1 letters are valued 1, and the rest are 0s
        # S2 SELECTED letters are avlued 1 and rest are 0

        # if s1 is longer than the string being compared to
        if len(s1) > len(s2):
            return False

        # init empty arrays
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Locate and Map each char
        # go through each character in s1
        # get the amount of chars in s1
            # THIS RANGE STARTS AT 0 AND GOES TO X
            # SLIDING WINDOW CONTINUES AFTER IT
        for i in range(len(s1)):

            # go through each NUMBER in the range made
            # find the related ascii for char at indx
            # subtract that from ascii 'a', to get 0 indexed alphabet
            # increment found indx by 1
            s1Count[ord(s1[i]) - ord('a')] += 1
            
            # same process for string being compared to
            s2Count[ord(s2[i]) - ord('a')] += 1

        # MATCHING
        # init number of matches
        matches = 0

        # 26 spots in array, one for each letter
        for i in range(26):
            # Add 1, IF
            # ascii matches, otherwise add nothing
            matches += (1 if s1Count[i] == s2Count[i] else 0)


        # SLIDING WINDOW
        # Start at beginning
        l = 0
        # use RIGHT pointer
            # START AT THE ENDING OF S1 (X) AND GO TO THE END OF S2
        for r in range(len(s1), len(s2)):
            # if MATCH was immediately succesful, return true
            if matches == 26:
                return True
            
            # --- 1. ADD NEW CHARACTER ON THE RIGHT (s2[r]) ---
            # Get 0-25 index for the character entering the window
            index = ord(s2[r]) - ord('a')
            
            # Add it to our current window count
            s2Count[index] += 1
            
            # If adding this character made its count PERFECTLY MATCH s1's count, gain a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it WAS matching before we incremented it, we just ruined the match, lose a match
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

        

            # --- 2. REMOVE OLD CHARACTER ON THE LEFT (s2[l]) ---
            # Get 0-25 index for the character leaving the window
            index = ord(s2[l]) - ord('a')
            
            # Remove it from our current window count
            s2Count[index] -= 1
            
            # If removing this character brought its count back into PERFECT MATCH with s1, gain a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it WAS matching before we decremented it, we just broke the match, lose a match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # Slide the left boundary rightward to maintain window size equal to len(s1)
            l += 1
            
        # Final check for the very last window position after the loop finishes
        return matches == 26