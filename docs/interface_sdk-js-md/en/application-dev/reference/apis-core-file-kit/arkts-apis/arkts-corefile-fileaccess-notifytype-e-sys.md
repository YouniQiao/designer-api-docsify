# NotifyType (System API)

枚举，通知类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

<!--Device-fileAccess-enum NotifyType--><!--Device-fileAccess-enum NotifyType-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_ADD

```TypeScript
NOTIFY_ADD = 0
```

表示新增文件（详见registerObserver接口的示例2、示例3）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_ADD = 0--><!--Device-NotifyType-NOTIFY_ADD = 0-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_DELETE

```TypeScript
NOTIFY_DELETE = 1
```

表示删除文件（详见unregisterObserver(uri: string, callback: Callback&lt;NotifyMessage&gt;)接口的示例1、示例2）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_DELETE = 1--><!--Device-NotifyType-NOTIFY_DELETE = 1-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_MOVED_TO

```TypeScript
NOTIFY_MOVED_TO = 2
```

表示移动至该文件（对目录下子文件或目录执行rename操作，或外部文件或目录执行move操作到本文件。详见registerObserver接口的示例1，及unregisterObserver(uri: string)接口的示例1）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_MOVED_TO = 2--><!--Device-NotifyType-NOTIFY_MOVED_TO = 2-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_MOVED_FROM

```TypeScript
NOTIFY_MOVED_FROM = 3
```

表示自该文件移出（对目录下子文件或目录执行rename操作，或子文件（夹）执行move操作从该文件夹内移出。详见registerObserver接口的示例1，及unregisterObserver(uri: string)接口的示例1）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_MOVED_FROM = 3--><!--Device-NotifyType-NOTIFY_MOVED_FROM = 3-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_MOVE_SELF

```TypeScript
NOTIFY_MOVE_SELF = 4
```

表示本文件被移动（如对文件或文件夹执行rename或move操作时，监听该文件（夹）的callback收到该事件，详见registerObserver接口的示例1）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_MOVE_SELF = 4--><!--Device-NotifyType-NOTIFY_MOVE_SELF = 4-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_DEVICE_ONLINE

```TypeScript
NOTIFY_DEVICE_ONLINE = 5
```

表示设备上线。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_DEVICE_ONLINE = 5--><!--Device-NotifyType-NOTIFY_DEVICE_ONLINE = 5-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## NOTIFY_DEVICE_OFFLINE

```TypeScript
NOTIFY_DEVICE_OFFLINE = 6
```

表示设备下线。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotifyType-NOTIFY_DEVICE_OFFLINE = 6--><!--Device-NotifyType-NOTIFY_DEVICE_OFFLINE = 6-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

