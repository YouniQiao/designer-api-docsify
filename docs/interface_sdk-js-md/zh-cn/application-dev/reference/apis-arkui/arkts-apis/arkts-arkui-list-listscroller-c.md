# ListScroller

List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

> **说明：**&gt;
> ListScroller继承自Scroller，具有Scroller的全部方法。

**继承/实现关系：** ListScroller extends Scroller

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

将EXPANDED状态的ListItem收起，并设置回调事件。<p>&lt;strong&gt;注意&lt;/strong&gt;： <br>-一个&lt;em&gt;ListScroller&lt;/em&gt;必须绑定到&lt;em&gt;List&lt;/em&gt;组件。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-arkui-list-closeswipeactionoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: int, indexInGroup: int): RectResult
```

获取ListItemGroup中的ListItem的大小和相对于List的位置。<p>&lt;strong&gt;注意&lt;/strong&gt;： <br>-&lt;em&gt;index&lt;/em&gt;的值必须是显示区域中可见的子组件的索引。 否则，该值将被视为无效值。 <br>-设置&lt;em&gt;index&lt;/em&gt;的子组件必须是列表项组。否则， &lt;em&gt;index &lt;/em&gt;值被认为是无效的。 <br>-&lt;em&gt;indexInGroup&lt;/em&gt;的值必须是列表项组中某个列表项的索引 在显示区域中可见。否则，该值将被视为无效值。 <br>-当&lt;em&gt;index&lt;/em&gt;或&lt;em&gt;indexInGroup&lt;/em&gt;设置为无效值时，返回的大小和位置均为&lt;em&gt;0&lt;/em&gt;。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| indexInGroup | int | 是 |

**返回值：**

| 类型 |
| --- |
| [RectResult](../arkts-components/arkts-arkui-rectresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo
```

根据坐标获取子组件的索引信息。<p>&lt;strong&gt;注意&lt;/strong&gt;： <br>-如果提供的&lt;em&gt;x&lt;/em&gt;或&lt;em&gt;y&lt;/em&gt;的值无效， 返回的VisibleListContentInfo对象的&lt;em&gt;index&lt;/em&gt;属性设置为&lt;em&gt;-1&lt;/em&gt;。 且&lt;em&gt;itemGroupArea&lt;/em&gt;和&lt;em&gt;itemIndexInGroup&lt;/em&gt;均为&lt;em&gt;未定义&lt;/em&gt;。 </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

**返回值：**

| 类型 |
| --- |
| [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void
```

滑动到指定的ListItemGroup中指定的ListItem。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| indexInGroup | int | 是 |
| smooth | boolean | 否 |
| align | [ScrollAlign](../arkts-components/arkts-arkui-scrollalign-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |
