# getSessionDescriptors（系统接口）

## getSessionDescriptors

```TypeScript
function getSessionDescriptors(category: SessionCategory): Promise<Array<Readonly<AVSessionDescriptor>>>
```

根据不同的会话类别获取对应的会话描述。使用Promise异步回调。

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getSessionDescriptors(category: SessionCategory): Promise<Array<Readonly<AVSessionDescriptor>>>--><!--Device-avSession-function getSessionDescriptors(category: SessionCategory): Promise<Array<Readonly<AVSessionDescriptor>>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [category](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioeffectproperty-i-sys.md) | [SessionCategory](arkts-avsession-avsession-sessioncategory-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Readonly&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.getSessionDescriptors(avSession.SessionCategory.CATEGORY_ALL).then((descriptors: avSession.AVSessionDescriptor[]) => {
  console.info(`Succeeded in getting session descriptors, length: ${descriptors.length}`);
  if (descriptors.length > 0) {
    console.info(`Succeeded in getting session descriptor, isActive: ${descriptors[0].isActive}`);
    console.info(`Succeeded in getting session descriptor, type: ${descriptors[0].type}`);
    console.info(`Succeeded in getting session descriptor, sessionTag: ${descriptors[0].sessionTag}`);
  }
});
```
