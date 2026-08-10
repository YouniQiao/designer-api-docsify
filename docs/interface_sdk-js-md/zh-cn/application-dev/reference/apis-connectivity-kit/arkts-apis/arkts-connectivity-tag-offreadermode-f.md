# offReaderMode

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## offReaderMode

```TypeScript
function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void
```

Disable foreground reader mode settings explicitly.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void--><!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 | The element name of application, must include the bundleName and abilityName. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TagInfo&gt; | 否 | The callback to dispatched the TagInfo object for application. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100203 | The off() API can be called only when the on() has been called. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

