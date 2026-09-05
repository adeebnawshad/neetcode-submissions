class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0
        let r = nums.length - 1
        while (l < r) {
            let mid = Math.floor((l + r)/2);
            if (nums[mid] > nums[r]) { // mid is in left sorted portion, min is in right sorted portion
                l = mid + 1;
            }
            else { // mid is in the right sorted portion, so min is at mid or before mid, as min must be in the right sorted portion (if fully sorted array, the whole array is the right sorted portion)
                r = mid;
            }
        }
        let minIdx = l

        const binarySearch = (l, r) => {
            while (l <= r) {
                let mid = Math.floor((l + r)/2);
                if (nums[mid] === target) {
                    return mid
                }
                else if (target < nums[mid]) { // target is in the left subarray
                    r = mid - 1
                }
                else {
                    l = mid + 1
                }
            }
            return -1
        }
        let res = binarySearch(0, l - 1)
        if (res !== -1) {
            return res
        }
        
        return binarySearch(l, nums.length - 1) 
    }
}
