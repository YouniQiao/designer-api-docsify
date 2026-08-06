# TaskState

Upload task information, which is the callback parameter of the  
[on('complete' | 'fail')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_and  
[off('complete' | 'fail')]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_APIs.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-request-interface TaskState--><!--Device-request-interface TaskState-End-->

**System capability:** SystemCapability.MiscServices.Upload

## message

```TypeScript
message: string
```

Description of the upload task result.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-message: string--><!--Device-TaskState-message: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## path

```TypeScript
path: string
```

File path.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-path: string--><!--Device-TaskState-path: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## responseCode

```TypeScript
responseCode: int
```

Return value of an upload task. The value **0** means that the task is successful, and other values means that the task fails. For details about the task result, see **message**.

You are advised to create an upload task by using  
[request.agent.create]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_and handle exceptions based on standard error codes.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-responseCode: int--><!--Device-TaskState-responseCode: int-End-->

**System capability:** SystemCapability.MiscServices.Upload

