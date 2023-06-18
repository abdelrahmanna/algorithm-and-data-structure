import java.util.Iterator;
import java.util.LinkedList;

class HashSet {

    private LinkedList<Integer>[] hashSet;
    private final short numberOfBuckets = 24;

    public HashSet() {
        hashSet = new LinkedList[numberOfBuckets];
    }

    public void add(int key) {
        if (hashSet[hashFunction(key)] == null) {
            hashSet[hashFunction(key)] = new LinkedList<Integer>();
        }

        if (!contains(key)) {
            hashSet[hashFunction(key)].add(key);
        }
    }

    public void remove(int key) {
        int hashedKey = hashFunction(key);

        if (hashSet[hashedKey] == null) {
            return;
        }

        int binSize = hashSet[hashedKey].size();

        if (binSize > 0) {
            Iterator iterator = hashSet[hashedKey].iterator();
            while (iterator.hasNext()) {
                int existingKey = (int) iterator.next();
                if (existingKey == key) {
                    iterator.remove();
                    break;
                }
            }

        }
    }

    public boolean contains(int key) {
        int hashedKey = hashFunction(key);
        if (hashSet[hashedKey] == null) {
            return false;
        }
        int binSize = hashSet[hashedKey].size();

        if (binSize > 0) {
            boolean keyExists = false;
            Iterator iterator = hashSet[hashedKey].iterator();
            while (iterator.hasNext()) {
                int existingKey = (int) iterator.next();
                if (existingKey == key) {
                    keyExists = true;
                    break;
                }
            }
            if (keyExists) {
                return true;
            }
        }

        return false;
    }

    private int hashFunction(int key) {

        return key % numberOfBuckets;
    }
}
