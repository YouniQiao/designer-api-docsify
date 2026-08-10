# onSelectionComplete

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与[offSelectionComplete](selectionManager.offSelectionComplete(callback?: Callback&lt;SelectionInfo&gt;))搭配使用取消订阅。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SelectionInfo&gt; | 是 | 回调函数，返回划词事件信息[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)。该回 调仅在用户通过鼠标或触控板选中文本（双击/三击/滑动）后按下Ctrl键时触发。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 33600003 | The application calling the API does not match the application selected in the system settings. |

