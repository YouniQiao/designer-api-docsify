# onAttachmentDidFail

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## onAttachmentDidFail

```TypeScript
function onAttachmentDidFail(callback: Callback<AttachFailureReason>): void
```

订阅绑定失败事件。使用callback异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md)&gt; | 是 |
