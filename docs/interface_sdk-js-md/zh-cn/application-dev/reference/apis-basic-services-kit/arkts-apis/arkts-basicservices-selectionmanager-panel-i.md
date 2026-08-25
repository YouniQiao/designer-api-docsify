# Panel

划词面板对象，通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)创建，提供面板内容设置、显示、隐藏、移动及事件订阅等管理能力，适用于在划词完成后向用户展示自定义操作界面的场景。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## hide

```TypeScript
hide(): Promise<void>
```

隐藏当前划词面板，与[show](#show)搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到 Panel实例后调用。使用Promise异步回调。如不主动调用，面板在失焦时会自动隐藏。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../errorcode-selection.md#33600002-划词面板已被销毁) |

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

移动划词面板至屏幕全局坐标系下的指定位置，支持移动到扩展屏上。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../errorcode-selection.md#33600002-划词面板已被销毁) |

## off('destroyed')

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

取消订阅划词面板销毁事件，与on('destroyed')搭配使 用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'destroyed' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('hidden')

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

取消订阅划词面板隐藏事件，与on('hidden')搭配使用。需通过 [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hidden' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## on('destroyed')

```TypeScript
on(type: 'destroyed', callback: Callback<void>): void
```

订阅划词面板销毁事件，与off('destroyed')搭配使 用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'destroyed' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('hidden')

```TypeScript
on(type: 'hidden', callback: Callback<void>): void
```

订阅划词面板隐藏事件，与off('hidden')搭配使用。面板调用 [hide](#hide)隐藏或失焦自动隐藏时触发该事件。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到 Panel实例后调用。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hidden' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

为当前的划词面板设置界面内容，例如展示翻译结果、搜索建议或自定义操作按钮等。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。使用Promise 异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../errorcode-selection.md#33600002-划词面板已被销毁) |

## show

```TypeScript
show(): Promise<void>
```

显示划词面板，与[hide](#hide)搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到 Panel实例后调用。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../errorcode-selection.md#33600002-划词面板已被销毁) |

## startMoving

```TypeScript
startMoving(): Promise<void>
```

设置划词面板可随鼠标、触控板或触屏拖动移动位置，指针释放后自动停止移动。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)获取到Panel实例后调用。使用Promise异步 回调。该接口需在onTouch的回调函数中调用，并且事件类型为TouchType.Down。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../errorcode-selection.md#33600002-划词面板已被销毁) |
