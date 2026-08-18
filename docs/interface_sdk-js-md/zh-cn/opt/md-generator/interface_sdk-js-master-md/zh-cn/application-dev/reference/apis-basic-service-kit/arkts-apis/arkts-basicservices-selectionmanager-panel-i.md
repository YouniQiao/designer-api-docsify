# Panel（系统接口）

划词面板对象，通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)创建，提供面板内容设置、显示、隐藏、移动及事件订阅等管理能力，适用于在划词完成后向用户展示自定义操作界面的场景。

**起始版本：** 24

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

移动划词面板至屏幕全局坐标系下的指定位置，支持移动到扩展屏上。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)获取到Panel实例后调用。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

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
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-划词服务调用异常) |
| [33600002](../../apis-basic-services-kit/errorcode-selection.md#33600002-划词面板已被销毁) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 移动划词面板至屏幕指定位置。selectionPanel为createPanel创建出的panel实例
  selectionPanel.moveToGlobalDisplay(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
}
```

## offDestroy

```TypeScript
offDestroy(callback?: Callback<void>): void
```

取消订阅划词面板销毁事件，与[onDestroy](#ondestroy)搭配使用。需通过 [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)获取到Panel实例后调用。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## offHide

```TypeScript
offHide(callback?: Callback<void>): void
```

取消订阅划词面板隐藏事件，与[onHide](#onhide)搭配使用。需通过 [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)获取到Panel实例后调用。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## onDestroy

```TypeScript
onDestroy(callback: Callback<void>): void
```

订阅划词面板销毁事件，与[offDestroy](#offdestroy)搭配使用。需通过 [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)获取到Panel实例后调用。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## onHide

```TypeScript
onHide(callback: Callback<void>): void
```

订阅划词面板隐藏事件，与[offHide](#offhide)搭配使用。需通过 [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)获取到Panel实例后调用。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |
