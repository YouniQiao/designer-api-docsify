# ZoomQuery

提供了与设备的缩放相关的查询功能，包括获取支持的缩放比例范围。

> **说明：**
> 
> - 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

**起始版本：** 12

<!--Device-camera-interface ZoomQuery--><!--Device-camera-interface ZoomQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## isZoomCenterPointSupported

```TypeScript
isZoomCenterPointSupported(): boolean
```

Checks whether zoom center point is supported.

**起始版本：** 20

<!--Device-ZoomQuery-isZoomCenterPointSupported(): boolean--><!--Device-ZoomQuery-isZoomCenterPointSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
