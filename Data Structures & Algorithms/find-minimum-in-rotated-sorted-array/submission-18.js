class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
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
        return nums[l];
    }
}
