/*
 * Copyright 2011 Vincent Buzzano
 * 
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package play.modules.gwt2;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * GWT2EnableAsync Annotation
 * 
 * Add to GWT2Service a way to be executed async using PlayJob * 
 * 
 * @author Vincent Buzzano <vincent.buzzano@gmail.com>
 *
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface GWT2EnableAsync {
   
	/**
	 *
	 * GLOBAL = run the service as a Job
	 * INTERN = enable the service to use await command
	 */
	public static enum Enable {
		GLOBAL,
		INTERN
	}
	
	/**
	 * Value can be
	 * 
	 * @return
	 */
	public String value();    
}
