# getDeviceList

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceList

```TypeScript
function getDeviceList(callback: AsyncCallback<Array<number>>): void
```

获取所有输入设备的ID列表，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getDeviceList

```TypeScript
function getDeviceList(): Promise<Array<number>>
```

获取所有输入设备的ID列表，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |
