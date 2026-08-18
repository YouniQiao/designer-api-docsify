# RootIterator (System API)

Provides an iterator object of the device root directory.

**Since:** 9

**Deprecated since:** 23

<!--Device-fileAccess-interface RootIterator--><!--Device-fileAccess-interface RootIterator-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## next

```TypeScript
next(): { value: RootInfo, done: boolean }
```

Obtains the next-level root directory.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-RootIterator-next(): { value: RootInfo, done: boolean }--><!--Device-RootIterator-next(): { value: RootInfo, done: boolean }-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| { value: RootInfo, done: boolean } |

**Error codes:**

| Error Code ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |
