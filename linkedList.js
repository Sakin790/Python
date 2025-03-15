class Node {
  constructor(item = null, next = null) {
    this.item = item;
    this.next = next;
  }
}

class SSL {
  constructor(start = null) {
    this.start = start;
  }
  isEmpty() {
    return this.start === null;
  }
}
