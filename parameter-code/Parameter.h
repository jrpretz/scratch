#ifndef PARAMETER_H
#define PARAMETER_H

#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <string>

/**
 * A simple class for wrapping class getters and setters so they 
 * can be dealt with agnostically by other code.
 *
 * Thinking mostly minimizers or fitters that don't want to know the details
 * of a class's parameters. Just how to change them.
 **/
class Parameter{
public:
  typedef boost::function<double ()> Getter;
  typedef boost::function<void (double)> Setter;

  template <class T>
  Parameter(T* instance,
            void (T::*setterIn)(double),
            double (T::*getterIn)(void) const,
            const std::string& pname){

    setter = boost::bind(setterIn,instance,_1);
    getter = boost::bind(getterIn,instance);
    name = pname;
  }

  Parameter(){}

  Setter setter;
  Getter getter;
  std::string name;

};



#endif
