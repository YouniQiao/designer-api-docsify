# X500DistinguishedName

提供X.500可分辨名称操作的API。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cert-interface X500DistinguishedName--><!--Device-cert-interface X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

获取X.500可分辨名称的DER编码数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getEncoded(): EncodingBlob--><!--Device-X500DistinguishedName-getEncoded(): EncodingBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) | X.500可分辨名称的DER编码数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getName

```TypeScript
getName(): string
```

获取可分辨名的字符串。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getName(): string--><!--Device-X500DistinguishedName-getName(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 可分辨名的字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getName

```TypeScript
getName(encodingType: EncodingType): string
```

根据指定编码格式获取可分辨名称的字符串。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string--><!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | 表示编码格式。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示可分辨名称的字符串，使用逗号分隔相对可分辨名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020003 | 参数检查失败。可能的原因： &lt;br&gt;1. encodingType的值不在EncodingType枚举范围内。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getName

```TypeScript
getName(type: string): Array<string>
```

按指定类型获取相对可分辨名称的字符串。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getName(type: string): Array<string>--><!--Device-X500DistinguishedName-getName(type: string): Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 指定类型的名称。如"CN"、"OU"等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 相对可分辨名称的字符串数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getName

```TypeScript
getName(type: string, encodingType: EncodingType): Array<string>
```

根据指定类型和编码格式获取相对可分辨名称的字符串数组。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>--><!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 指定类型的名称。如"CN"、"OU"等。 |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | 表示编码格式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 相对可分辨名称的字符串数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020003 | 参数检查失败。可能的原因： &lt;br&gt;1. encodingType的值不在EncodingType枚举范围内。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

