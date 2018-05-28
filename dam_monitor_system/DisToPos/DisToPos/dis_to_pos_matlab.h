//
// MATLAB Compiler: 6.2 (R2016a)
// Date: Fri May 25 17:06:02 2018
// Arguments: "-B" "macro_default" "-W" "cpplib:dis_to_pos_matlab" "-T"
// "link:lib" "dis_to_pos_matlab" 
//

#ifndef __dis_to_pos_matlab_h
#define __dis_to_pos_matlab_h 1

#if defined(__cplusplus) && !defined(mclmcrrt_h) && defined(__linux__)
#  pragma implementation "mclmcrrt.h"
#endif
#include "mclmcrrt.h"
#include "mclcppclass.h"
#ifdef __cplusplus
extern "C" {
#endif

#if defined(__SUNPRO_CC)
/* Solaris shared libraries use __global, rather than mapfiles
 * to define the API exported from a shared library. __global is
 * only necessary when building the library -- files including
 * this header file to use the library do not need the __global
 * declaration; hence the EXPORTING_<library> logic.
 */

#ifdef EXPORTING_dis_to_pos_matlab
#define PUBLIC_dis_to_pos_matlab_C_API __global
#else
#define PUBLIC_dis_to_pos_matlab_C_API /* No import statement needed. */
#endif

#define LIB_dis_to_pos_matlab_C_API PUBLIC_dis_to_pos_matlab_C_API

#elif defined(_HPUX_SOURCE)

#ifdef EXPORTING_dis_to_pos_matlab
#define PUBLIC_dis_to_pos_matlab_C_API __declspec(dllexport)
#else
#define PUBLIC_dis_to_pos_matlab_C_API __declspec(dllimport)
#endif

#define LIB_dis_to_pos_matlab_C_API PUBLIC_dis_to_pos_matlab_C_API


#else

#define LIB_dis_to_pos_matlab_C_API

#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_dis_to_pos_matlab_C_API 
#define LIB_dis_to_pos_matlab_C_API /* No special import/export declaration */
#endif

extern LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV dis_to_pos_matlabInitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV dis_to_pos_matlabInitialize(void);

extern LIB_dis_to_pos_matlab_C_API 
void MW_CALL_CONV dis_to_pos_matlabTerminate(void);



extern LIB_dis_to_pos_matlab_C_API 
void MW_CALL_CONV dis_to_pos_matlabPrintStackTrace(void);

extern LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV mlxDis_to_pos_matlab(int nlhs, mxArray *plhs[], int nrhs, mxArray 
                                       *prhs[]);


#ifdef __cplusplus
}
#endif

#ifdef __cplusplus

/* On Windows, use __declspec to control the exported API */
#if defined(_MSC_VER) || defined(__BORLANDC__)

#ifdef EXPORTING_dis_to_pos_matlab
#define PUBLIC_dis_to_pos_matlab_CPP_API __declspec(dllexport)
#else
#define PUBLIC_dis_to_pos_matlab_CPP_API __declspec(dllimport)
#endif

#define LIB_dis_to_pos_matlab_CPP_API PUBLIC_dis_to_pos_matlab_CPP_API

#else

#if !defined(LIB_dis_to_pos_matlab_CPP_API)
#if defined(LIB_dis_to_pos_matlab_C_API)
#define LIB_dis_to_pos_matlab_CPP_API LIB_dis_to_pos_matlab_C_API
#else
#define LIB_dis_to_pos_matlab_CPP_API /* empty! */ 
#endif
#endif

#endif

extern LIB_dis_to_pos_matlab_CPP_API void MW_CALL_CONV dis_to_pos_matlab(int nargout, mwArray& xyz, const mwArray& x1, const mwArray& x2, const mwArray& x3, const mwArray& x4, const mwArray& x5, const mwArray& x6, const mwArray& x7, const mwArray& x8, const mwArray& x9, const mwArray& x10, const mwArray& x11, const mwArray& x12, const mwArray& da, const mwArray& db, const mwArray& dc, const mwArray& dd);

#endif
#endif
