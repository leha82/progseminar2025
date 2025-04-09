public class ourPassword_HS {
    public static String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        String alphabet = "abcdefghijklmnopqrstuvwxyz";


        for (char c : skip.toCharArray()) {
            alphabet = alphabet.replace(String.valueOf(c), "");
        }

        for (char c : s.toCharArray()) {
            int pos = alphabet.indexOf(c);
            int newIndex = (pos + index) % alphabet.length();
            answer.append(alphabet.charAt(newIndex));
        }

        return answer.toString();
    }

    public static void main(String[] args) {
        String s = "aukks";
        String skip = "wbqd";
        int index = 5;

        String result = solution(s, skip, index);
        System.out.println("result: " + result);
    }
}
