class Solution (object):
    def twoSum (self, nums, target): 
        # self = is required
        # nums = is our list of numberts (like[1,2,3,4])
        # target = is the number we wanna to reach (like 9)

        seen = {}
        # an enpty dictionary 

        for i, num in enumerate(nums):
            # "enumerate(nums)"" gives us both, the POSITION = "i", and the VALUE = "num".
            # E.g. [55, 0, 607....] 
            # the firsy loop gives us the [0, 55]

            needed = target - num 
            # Calculate what nubmer we need to complete the pair  
            # E.g. if current nnumber is 2, and the target is 9 
            # We need 9 - 2 = 7


            if needed in seen: 
                # check of this needed number exists in our dictionary

                return[seen[needed], i]
                # Return the positions of numbers 
                # "[seen[needed]]" gives the positon where we saw the "needednumber"
                # "i" is the current Position 
                # So we return [position_of_needed, current_position]

            seen[num] = i
            # if we didn't find the pair yer, store current number
            # add this nubmer to our dictionary so we remeber we so it

        return []
    # This line runs only we NO solution is found 
    # But the problam says there is always the solution, so we don't reach here


# Test your function
# Create an instance of the Solution class called 'sol'
# This lets us use the twoSum method inside it
sol = Solution()

# Call the twoSum method with list [2,7,11,15] and target 9
# Should return [0,1] because 2 (index 0) + 7 (index 1) = 9
print(sol.twoSum([2,7,11,15], 9))  # Expected: [0,1]

# Call twoSum again with different input: [3,2,4] and target 6
# Should return [1,2] because 2 (index 1) + 4 (index 2) = 6
print(sol.twoSum([3,2,4], 6))      # Expected: [1,2]