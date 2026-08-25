# MifareUltralightTag

MifareUltralightTag 提供对MIFARE Ultralight属性和I/O操作的访问，继承自TagSession。TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](arkts-connectivity-tagsession-tagsession-i.md)。MifareUltralightTag获取方式请参考[nfc-tag开发指南](../../../connectivity/nfc/nfc-tag-access-guide.md)。以下是MifareUltralightTag的独有接口。

**继承/实现关系：** MifareUltralightTag extends TagSession

**起始版本：** 9

**系统能力：** SystemCapability.Communication.NFC.Tag

## getType

```TypeScript
getType(): tag.MifareUltralightType
```

获取MIFARE Ultralight标签的类型。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| tag.MifareUltralightType |

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number): Promise<number[]>
```

读取标签的4页数据，共16字节的数据。每个页面数据大小为4字节。使用Promise异步回调

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void
```

读取标签的4页数据，共16字节的数据。每个页面数据大小为4字节。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[]): Promise<void>
```

写入一页数据，数据大小为4字节。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |
| data | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void
```

写入一页数据，数据大小为4字节。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |
| data | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |
