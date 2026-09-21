# ArcAlphabetIndexer

弧形索引条是一种弧形的、可按字母顺序排序进行快速定位的组件，可以与容器组件联动，按逻辑结构快速定位至容器显示区域。

> **说明：**

> - 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 子组件

无

## ArcAlphabetIndexer

```TypeScript
ArcAlphabetIndexer(info: ArcAlphabetIndexerInitInfo)
```

创建并初始化弧形索引条组件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [ArcAlphabetIndexerInitInfo](arkts-arkui-arcalphabetindexer-comp-arcalphabetindexerinitinfo-i.md) | 是 | 定义弧形字母索引条的初始化参数，包含字母索引字符串数组和初始选中项索引值。 |

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [ArcAlphabetIndexerInitInfo](arkts-arkui-arcalphabetindexer-comp-arcalphabetindexerinitinfo-i.md) | 定义弧形字母索引条的初始化参数。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnSelectCallback](arkts-arkui-arcalphabetindexer-comp-onselectcallback-t.md) | 定义[onSelect](arkts-arkui-arcalphabetindexer-comp-attribute.md#onselect)中使用的回调类型。 |

## 示例

```TypeScript
### 示例1（设置联动控制和定位）

该示例实现了弧形索引条和弧形列表联动控制和定位。


```

```TypeScript
### 示例2（设置弹窗显示）

该示例通过[popupColor](#popupcolor)和[popupBackground](#popupbackground)接口实现了提示弹窗的显示背景颜色和文字颜色。

从API version 18开始，支持popupColor和popupBackground接口。
```
