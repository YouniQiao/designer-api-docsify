# exportKey

## 导入模块

```TypeScript
```

## exportKey

```TypeScript
function exportKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

导出密钥，使用Callback方式回调异步返回的结果。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [huks.exportKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem)(keyAlias: string, options: HuksOptions, callback: AsyncCallback&lt;HuksReturnResult&gt;)

<!--Device-huks-function exportKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function exportKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; | 是 |

**示例**

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.exportKey(keyAlias, emptyOptions, (err, data) => {
});
```


## exportKey

```TypeScript
function exportKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>
```

导出密钥。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [huks.exportKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem)(keyAlias: string, options: HuksOptions)

<!--Device-huks-function exportKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function exportKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; |

**示例**

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.exportKey(keyAlias, emptyOptions);
```
