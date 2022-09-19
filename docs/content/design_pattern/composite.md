# 组合模式

## 1 概念

&emsp;&emsp;组合模式（Composite）是将对象组合成树形结构以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性。

## 2 知识点

&emsp;&emsp;组合模式主要包括三个对象，分别是Component（对象接口）、Composite（枝节点）和 Leaf（叶节点）
- Component（对象接口）：主要实现所有类共有接口的默认行为，声明一个接口，用于访问和管理 Component 的子部件
- Composite（枝节点）：定义枝节点行为，用于存储子部件，在 Component 接口中实现与子部件有关的操作，比如增加（Add）和删除（Remove）
- Leaf（叶节点）：表示叶节点对象，叶节点没有子节点