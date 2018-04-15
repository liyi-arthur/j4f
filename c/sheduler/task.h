/**
 * @file   task.h
 * @brief  
 * @authur Arthur Lee, liyi_whu@163.com
 * @version  1.0.0
 * @date  2018-04-15
 */

#ifndef __TASK_H__
#define __TASK_H__

#include <stdint.h>
#include "list.h"

typedef enum
{
    TASK_STATE_WAIT = 0,
    TASK_STATE_RUNNING,
    TASK_STATE_BUTT
} TASK_STATE_E;

typedef struct tagTASK_S
{
    struct list_head  sibling;  /**< task queue node */
    uint32_t          type;
    TASK_STATE_E      state;     
} TASK_S;

typedef struct tagSTEP_S
{
	uint32_t    id;
	uint32_t    retryTimes;
	uint32_t    retryDelay;
}STEP_S;

typedef struct tagTASK_REG_PARAM_S
{
	
} TASK_REG_PARAM_S;

int32_t regTask(uint32_t type, );
void unRegTask();

#endif	// __TASK_H__
