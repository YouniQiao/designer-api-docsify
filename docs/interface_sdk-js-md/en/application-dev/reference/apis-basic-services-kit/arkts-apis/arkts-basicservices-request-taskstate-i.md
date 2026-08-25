# TaskState

Upload task information, which is the callback parameter of the on('complete' | 'fail') and off('complete' | 'fail') APIs.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## message

```TypeScript
message: string
```

Description of the upload task result.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Upload

## path

```TypeScript
path: string
```

File path.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Upload

## responseCode

```TypeScript
responseCode: int
```

Return value of an upload task. The value **0** means that the task is successful, and other values means that the task fails. For details about the task result, see **message**.You are advised to create an upload task by using [request.agent.create](arkts-basicservices-agent-create-f.md)and handle exceptions based on standard error codes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Upload
