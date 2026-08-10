# onReaderModeWithInterval

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## onReaderModeWithInterval

```TypeScript
function onReaderModeWithInterval(
    elementName: ElementName,
    discTech: int[],
    callback: Callback<TagInfo>,
    interval: int
  ): void
```

Set reader mode enabled when the specific application is on foreground and set card presence interval.Tag infomation will be dispatched to the application only if a NFC tag is discovered.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void--><!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 | The element name of application, must include the bundleName and abilityName. |
| discTech | int[] | 是 | The technologies list to set for discovering. From {@link NFC_A} to {@link MIFARE_ULTRALIGHT}. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TagInfo&gt; | 是 | The callback to dispatched the TagInfo object for application. |
| interval | int | 是 | The interval for reader presence check. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3100202 | The element state is invalid. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

