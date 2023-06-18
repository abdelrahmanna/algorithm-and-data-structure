class HashMap {
    private Integer[][] hashMap;
    private final short numberOfBuckets = 2024;

    public HashMap() {
        hashMap = new Integer[numberOfBuckets][1000000 / numberOfBuckets + 1];
    }

    public int get(int key) {
        int bucketIndex = getBucketIndex(key);
        int itemIndex = getItemIndexInsideBucket(key, bucketIndex);
        return hashMap[bucketIndex][itemIndex] == null ? -1 : hashMap[bucketIndex][itemIndex];
    }

    public void put(int key, int value) {
        int bucketIndex = getBucketIndex(key);
        int itemIndex = getItemIndexInsideBucket(key, bucketIndex);

        hashMap[bucketIndex][itemIndex] = value;
    }

    public void remove(int key) {
        int bucketIndex = getBucketIndex(key);
        int itemIndex = getItemIndexInsideBucket(key, bucketIndex);

        hashMap[bucketIndex][itemIndex] = -1;
    }

    private int getBucketIndex(int key) {

        return key % numberOfBuckets;
    }

    private int getItemIndexInsideBucket(int key, int bucketIndex) {
        return (key - bucketIndex) / numberOfBuckets;
    }
}