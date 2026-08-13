# BackForwardList

Provides back and forward history list information method. related to [HistoryItem](arkts-arkweb-webview-historyitem-i.md#HistoryItem).

**起始版本：** 9

**废弃版本：** -1

<!--Device-webview-interface BackForwardList--><!--Device-webview-interface BackForwardList-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getItemAtIndex

```TypeScript
getItemAtIndex(index: number): HistoryItem
```

获取历史列表中指定索引的历史记录项信息。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BackForwardList-getItemAtIndex(index: number): HistoryItem--><!--Device-BackForwardList-getItemAtIndex(index: number): HistoryItem-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [HistoryItem](arkts-arkweb-webview-historyitem-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## currentIndex

```TypeScript
currentIndex: number
```

当前在页面历史列表中的索引。

**类型：** number

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BackForwardList-currentIndex: number--><!--Device-BackForwardList-currentIndex: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## size

```TypeScript
size: number
```

历史列表中索引的数量，最多保存50条，超过时起始记录会被覆盖。

**类型：** number

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BackForwardList-size: number--><!--Device-BackForwardList-size: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core
