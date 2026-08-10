# Panel

划词面板对象，通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)创建，提供面板内容设置、显示、隐藏、移动及事件订阅等管理能力，适用于在划词完成后向用户展示自定义操作界面的场景。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-selectionManager-interface Panel--><!--Device-selectionManager-interface Panel-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## hide

```TypeScript
hide(): Promise<void>
```

隐藏当前划词面板，与[show](arkts-basicservices-selectionmanager-panel-i.md#show)搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。如不主动调用，面板在失焦时会自动隐藏。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Hide the word selection panel. selectionPanel is a Panel instance created by createPanel.
selectionPanel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Error code: ${err.code}, error message: ${err.message}`);
});
```

## moveTo

```TypeScript
moveTo(x: int, y: int): Promise<void>
```

移动划词面板至屏幕全局坐标系下的指定位置，支持移动到扩展屏上。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。

> **说明：**
> 
> 从API version 20开始支持，从API version 24开始废弃。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 24

**Substitutes:** [selectionManager.Panel.moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | 目标位置在屏幕全局坐标系下的x轴坐标，单位为px。全局坐标系以主屏幕左上角为原点，x轴正方向向右；扩展屏的x坐标视屏幕布局可能为负值。 |
| y | int | Yes | 目标位置在屏幕全局坐标系下的y轴坐标，单位为px。全局坐标系以主屏幕左上角为原点，y轴正方向向下；扩展屏的y坐标视屏幕布局可能为负值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Move the word selection panel to the specified coordinates on the screen. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.moveTo(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
}
```

## moveToGlobalDisplay

ArkTS-Dyn:
```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
moveToGlobalDisplay(x: int, y: int): Promise<void>
```

移动划词面板至屏幕全局坐标系下的指定位置，支持移动到扩展屏上。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Panel-moveToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标位置在屏幕全局坐标系下的x轴坐标，单位为px。全局坐标系以主屏幕左上角为原点，x轴正方向向右；扩展屏的x坐标视屏幕布局可能为负值。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标位置在屏幕全局坐标系下的y轴坐标，单位为px。全局坐标系以主屏幕左上角为原点，y轴正方向向下；扩展屏的y坐标视屏幕布局可能为负值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Move the word selection panel to the specified coordinates on the screen. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.moveToGlobalDisplay(200, 200).then(() => {
    console.info('Succeeded in moving the panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to move panel. Error code: ${err.code}, error message: ${err.message}`);
}
```

## off('destroyed')

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

取消订阅划词面板销毁事件，与[on('destroyed')](selectionManager.Panel.on(type: 'destroyed', callback: Callback&lt;void&gt;))搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'destroyed', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | 取消订阅的事件类型，固定取值为'destroyed'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 需要取消的回调函数（即之前通过on方法订阅时的回调实例）。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
try {
  // Unsubscribe from the word selection panel destruction event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.off('destroyed');
} catch (err) {
  console.error(`Failed to unregister destroyed. Error code: ${err.code}, error message: ${err.message}`);
}
```

## off('hidden')

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

取消订阅划词面板隐藏事件，与[on('hidden')](selectionManager.Panel.on(type: 'hidden', callback: Callback&lt;void&gt;))搭配使用。需通过  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void--><!--Device-Panel-off(type: 'hidden', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | 取消订阅的事件类型，固定取值为'hidden'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 需要取消的回调函数（即之前通过on方法订阅时的回调实例）。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
try {
  // // Unsubscribe from the word selection panel hiding event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.off('hidden');
} catch (err) {
  console.error(`Failed to unregister hidden. Error code: ${err.code}, error message: ${err.message}`);
}
```

## offDestroy

```TypeScript
offDestroy(callback?: Callback<void>): void
```

取消订阅划词面板销毁事件，与[onDestroy](selectionManager.Panel.onDestroy(callback: Callback&lt;void&gt;))搭配使用。需通过  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offDestroy(callback?: Callback<void>): void--><!--Device-Panel-offDestroy(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 需要取消的回调函数（即之前通过onDestroy方法订阅时的回调实例）。参数不填写时，取消订阅对应的所有回调事件。 |

## offHide

```TypeScript
offHide(callback?: Callback<void>): void
```

取消订阅划词面板隐藏事件，与[onHide](selectionManager.Panel.onHide(callback: Callback&lt;void&gt;))搭配使用。需通过  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 需要取消的回调函数（即之前通过onHide方法订阅时的回调实例）。参数不填写时，取消订阅对应的所有回调事件。 |

## on('destroyed')

```TypeScript
on(type: 'destroyed', callback: Callback<void>): void
```

订阅划词面板销毁事件，与[off('destroyed')](selectionManager.Panel.off(type: 'destroyed', callback?: Callback&lt;void&gt;))搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void--><!--Device-Panel-on(type: 'destroyed', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'destroyed' | Yes | 设置监听类型，固定取值为'destroyed'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数，调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel)销毁面板时触发。 |

## Examples

```TypeScript
try {
  // Subscribe to the word selection panel destruction event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.on('destroyed', () => {
    console.info('Panel has been destroyed.');
  });
} catch (err) {
  console.error(`Failed to register destroyed callback. Error code: ${err.code}, error message: ${err.message}`);
}
```

## on('hidden')

```TypeScript
on(type: 'hidden', callback: Callback<void>): void
```

订阅划词面板隐藏事件，与[off('hidden')](selectionManager.Panel.off(type: 'hidden', callback?: Callback&lt;void&gt;))搭配使用。面板调用  
[hide](arkts-basicservices-selectionmanager-panel-i.md#hide)隐藏或失焦自动隐藏时触发该事件。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void--><!--Device-Panel-on(type: 'hidden', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hidden' | Yes | 设置监听类型，固定取值为'hidden'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数，面板隐藏时触发。面板可通过调用[hide](arkts-basicservices-selectionmanager-panel-i.md#hide)主动隐藏，或在失焦时自动隐藏。 |

## Examples

```TypeScript
try {
  // Subscribe to the word selection panel hiding event. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.on('hidden', () => {
    console.info('Panel has been hidden.');
  });
} catch (err) {
  console.error(`Failed to register hidden callback. Error code: ${err.code}, error message: ${err.message}`);
}
```

## onDestroy

```TypeScript
onDestroy(callback: Callback<void>): void
```

订阅划词面板销毁事件，与[offDestroy](selectionManager.Panel.offDestroy(callback?: Callback&lt;void&gt;))搭配使用。需通过  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onDestroy(callback: Callback<void>): void--><!--Device-Panel-onDestroy(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数，调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel)销毁面板时触发。 |

## onHide

```TypeScript
onHide(callback: Callback<void>): void
```

订阅划词面板隐藏事件，与[offHide](selectionManager.Panel.offHide(callback?: Callback&lt;void&gt;))搭配使用。需通过  
[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数，面板隐藏时触发。面板可通过调用[hide](arkts-basicservices-selectionmanager-panel-i.md#hide)主动隐藏，或在失焦时自动隐藏。 |

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

为当前的划词面板设置界面内容，例如展示翻译结果、搜索建议或自定义操作按钮等。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 要加载到面板中的页面内容的路径，Stage模型下该路径需添加到工程的resources/base/profile/main_pages.json文件中，不支持FA模型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Load page content for the word selection panel. selectionPanel is a Panel instance created by createPanel.
  selectionPanel.setUiContent('pages/Index').then(() => {
    console.info('Succeeded in setting the content.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to setUiContent. Error code: ${err.code}, error message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to setUiContent. Error code: ${err.code}, error message: ${err.message}`);
}
```

## show

```TypeScript
show(): Promise<void>
```

显示划词面板，与[hide](arkts-basicservices-selectionmanager-panel-i.md#hide)搭配使用。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Show the word selection panel. selectionPanel is a Panel instance created by createPanel.
selectionPanel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Error code: ${err.code}, error message: ${err.message}`);
});
```

## startMoving

```TypeScript
startMoving(): Promise<void>
```

设置划词面板可随鼠标、触控板或触屏拖动移动位置，指针释放后自动停止移动。需通过[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)获取到Panel实例后调用。使用Promise异步回调。该接口需在onTouch的回调函数中调用，并且事件类型为TouchType.Down。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Panel-startMoving(): Promise<void>--><!--Device-Panel-startMoving(): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600002 | This selection window has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// This code must be placed in build() of the ArkUI page component. RelativeContainer is a built-in component of ArkUI. TouchEvent and TouchType are built-in types of ArkUI.
RelativeContainer() {
  /* 
   * Page layout content, which should be defined based on your actual needs.
   */
}
.onTouch((event: TouchEvent) => {
  if (event.type === TouchType.Down) {
    if (selectionPanel !== undefined) {
      // Enable the word selection panel to be dragged and moved with the mouse, touchpad, or touchscreen. selectionPanel is the panel instance created by createPanel.
      selectionPanel.startMoving().then(() => {
        console.info('Succeeded in startMoving the panel.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to startMoving panel. Error code: ${err.code}, error message: ${err.message}`);
      });
    }
  }
})
```

