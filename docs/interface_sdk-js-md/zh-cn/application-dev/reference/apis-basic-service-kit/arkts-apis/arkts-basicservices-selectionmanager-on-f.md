# on

## on('selectionCompleted')

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与  
[off('selectionCompleted')](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off)搭配使用取消订阅。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectionCompleted' | 是 | 设置监听类型，固定取值为'selectionCompleted'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)&gt; | 是 | 回调函数，返回划词事件信息[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md#SelectionInfo)。该回 调仅在用户通过鼠标或触控板选中文本（双击/三击/滑动）后按下Ctrl键时触发。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [33600003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) | The application calling the API does not match the application selected in the system settings. |

## 示例

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

try {
  // 订阅划词完成事件
  selectionManager.on('selectionCompleted', (info: selectionManager.SelectionInfo) => {
    console.info('Enter the callback function.');
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback. Error code: ${err.code}, error message: ${err.message}`);
}
```

