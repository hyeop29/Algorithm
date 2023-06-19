class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, target);
        return answer;
    }
    public void dfs(int[] arr, int total, int depth, int target){
        if(depth == arr.length){
            if(target == total){
                answer++;
            }
            return;
        }
        dfs(arr, total + arr[depth], depth + 1, target);
        dfs(arr, total - arr[depth], depth + 1, target);
    }
}
