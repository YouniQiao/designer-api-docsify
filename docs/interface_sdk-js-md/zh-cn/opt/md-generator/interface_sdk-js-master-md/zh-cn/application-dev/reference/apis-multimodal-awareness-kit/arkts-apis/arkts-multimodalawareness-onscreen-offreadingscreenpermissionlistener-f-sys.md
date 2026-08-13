# offReadingScreenPermissionListener（系统接口）

## offReadingScreenPermissionListener

```TypeScript
function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void
```

关闭屏幕内容访问权限监测。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_SCREEN_CONTENT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-onScreen-function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void--><!--Device-onScreen-function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ReadingScreenPermissionStatus](arkts-multimodalawareness-onscreen-readingscreenpermissionstatus-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import onScreen from "@ohos.multimodalAwareness.onScreen";
try {
  onScreen.offReadingScreenPermissionListener();
  console.info(`offReadingScreenPermissionListener succeeded.`);
} catch (err) {
  console.error('offReadingScreenPermissionListener failed, errCode = ' + err.code);
}
```
